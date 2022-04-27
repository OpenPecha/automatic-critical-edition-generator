import re
from typing import DefaultDict
import yaml
from antx import transfer


def get_syls(text):
    chunks = re.split('(་|།།|།|\n)',text)
    syls = []
    cur_syl = ''
    for chunk in chunks:
        if re.search('་|།།|།|\n',chunk):
            cur_syl += chunk
            syls.append(cur_syl)
            cur_syl = ''
        else:
            cur_syl += chunk
    if cur_syl:
        syls.append(cur_syl)
    return syls


def get_context(chunk, type_):
    chunk = chunk.replace(':', '')
    context = ''
    syls = get_syls(chunk)
    if len(syls) >= 4:
        if type_ == 'left':
            context = f"{''.join(syls[-4:])}"
        else:
            context = f"{''.join(syls[:4])}"
    else:
        context = chunk
    return context.strip()

def clean_note(note_text):
    noise_anns = ['«པེ་»', '«སྣར་»', '«སྡེ་»', '«ཅོ་»', '\(\d+\) ', ':']
    for noise_ann in noise_anns:
        note_text = re.sub(noise_ann, '', note_text)
    return note_text

def get_default_option(prev_chunk):
    default_option = ''
    if ':' in prev_chunk:
        default_option = re.search(':(.*)', prev_chunk,re.DOTALL).group(1)
    else:
        syls = get_syls(prev_chunk)
        if syls:
            default_option = syls[-1]
    return default_option

def get_note_options(default_option, note_chunk):
    note_chunk = re.sub('\(\d+\)', '', note_chunk)
    if "+" in note_chunk:
        default_option = ""
    note_chunk = re.sub("\+", "", note_chunk)
    pub_mapping = {
        '«པེ་»': 'peking',
        '«པེ»': 'peking',
        '«སྣར་»': 'narthang',
        '«སྣར»': 'narthang',
        '«སྡེ་»': 'derge',
        '«སྡེ»': 'derge',
        '«ཅོ་»': 'chone',
        '«ཅོ»': 'chone'
    }
    note_options = {
        'peking': '',
        'narthang': '',
        'derge': '',
        'chone': ''
    }
    note_parts = re.split('(«པེ་»|«སྣར་»|«སྡེ་»|«ཅོ་»|«པེ»|«སྣར»|«སྡེ»|«ཅོ»)', note_chunk)
    pubs = note_parts[1::2]
    notes = note_parts[2::2]
    for walker, (pub, note_part) in enumerate(zip(pubs, notes)):
        if note_part:
            note_options[pub_mapping[pub]] = note_part.replace('>', '')
        else:
            if notes[walker+1]:
                note_options[pub_mapping[pub]] = notes[walker+1].replace('>', '')
            else:
                note_options[pub_mapping[pub]] = notes[walker+2].replace('>', '')
    for pub, note in note_options.items():
        if "-" in note:
            note_options[pub] = ""
        if not note:
            note_options[pub] = default_option
    return note_options

def update_left_context(default_option, prev_chunk, chunk):
    left_context = re.sub(f'{default_option}$', '', prev_chunk)
    if "+" in chunk:
        left_context = prev_chunk
    return left_context

def get_alt_options(default_option,note_options):
    alt_options = []
    for note in set(note_options.values()):
        if note != default_option and note != "":
            alt_options.append(note)
    return alt_options        

def get_note_sample(prev_chunk, note_chunk, next_chunk,collated_text,prev_end):
    default_option = get_default_option(prev_chunk)
    prev_chunk = update_left_context(default_option, prev_chunk, note_chunk)
    prev_context = get_context(prev_chunk, type_= 'left')
    next_context = get_context(next_chunk, type_= 'right')
    note_options = get_note_options(default_option, note_chunk)
    note_options = dict(sorted(note_options.items()))
    alt_options = get_alt_options(default_option,note_options)
    note_span,prev_end = get_note_span(collated_text,note_chunk,prev_end)
    note = {
        "left_context":prev_context,
        "right_context":next_context,
        "default_option":default_option.replace("\n",""),
        "default_clone_option":default_option,
        "note_options":note_options,
        "alt_options":alt_options,
        "span":note_span
    }
    return note,prev_end

def get_notes(collated_text):
    cur_text_notes = []
    prev_end = 0
    chunks = re.split('(\(\d+\) <.+?>)', collated_text)
    prev_chunk = chunks[0]
    for chunk_walker, chunk in enumerate(chunks):
        try:
            next_chunk = chunks[chunk_walker+1]
        except:
            next_chunk = ''
        if re.search('\(\d+\) <.+?>', chunk):
            note,prev_end  = get_note_sample(prev_chunk, chunk, next_chunk,collated_text,prev_end)
            cur_text_notes.append(note)
            continue
        prev_chunk = chunk
    return cur_text_notes

def get_notes_samples(collated_text, note_samples, text_id):
    collated_text = collated_text.replace('\n', '')
    collated_text = re.sub('\d+-\d+', '', collated_text)
    cur_text_notes = get_notes(collated_text)
    for cur_text_note, note_options in cur_text_notes:
        if note_samples.get(cur_text_note, {}):
            note_samples[cur_text_note]['count'] += 1
            note_samples[cur_text_note]['text_id']=text_id
        else:
            note_samples[cur_text_note] = DefaultDict()
            note_samples[cur_text_note]['count'] = 1
            note_samples[cur_text_note]['text_id']=text_id
            note_samples[cur_text_note]['note_options'] = note_options
    return note_samples

def is_all_option_same(note_options):
    if note_options['derge'] == note_options['chone'] == note_options['peking'] == note_options['narthang']:
        return True
    else:
        return False

def get_note_context(note):
    right_context = ''
    left_context = ''
    if re.search(r'(.+)\[', note):
        left_context = re.search(r'(.+)\[', note).group(1)
    if re.search(r'\](.+)', note):
        right_context = re.search(r'\](.+)', note).group(1)
    return left_context, right_context

def get_sample_entry(note_walker, note, note_info):
    all_option_same_flag = is_all_option_same(note_info.get('note_options', {}))
    left_context, right_context = get_note_context(note)
    data_entry = [
        note_walker,
        '',
        left_context,
        note_info['note_options']['derge'],
        note_info['note_options']['chone'],
        note_info['note_options']['peking'],
        note_info['note_options']['narthang'],
        right_context,
        '',
        '',
        '',
        all_option_same_flag,
        note_info['count'],
        note_info['text_id'],
        ]
    return data_entry

def is_title_note(note):
    notes_options = []
    notes_options.append(note['note_options']['chone'])
    notes_options.append(note['note_options']['derge'])
    notes_options.append(note['note_options']['narthang'])
    notes_options.append(note['note_options']['peking'])
    
    right_context = note['right_context']
    left_context = note['left_context']
    left_context = re.sub(r"\xa0", " ", left_context)
    possible_left_texts = ["༄༅། །"]
    possible_right_texts = ["༄༅༅། །རྒྱ་གར་","༄༅། །རྒྱ་གར་","༅༅། །རྒྱ་གར་སྐད་དུ།","༄༅༅། ","༄༅༅།། །རྒྱ་གར་","ལྟར་བཀོད་ཅིང།"]
    
    
    for left_text in possible_left_texts:
        if left_text in left_context:
            return True
    for right_text in possible_right_texts:
        if right_text in right_context:
            for note_option in notes_options:
                if '༄༅།' in note_option:
                    return False
                else:
                    return True
    return False

def get_note_span(collated_text,chunk,prev_end):
    p = re.compile("\(.+?\) <.*?>")
    for m in p.finditer(collated_text):
        start,end = m.span()
        if m.group() in chunk and prev_end <= start:
            return m.span(),end


def get_default_word(collated_text, end_index, prev_end):
    if prev_end == None:
        prev_end = 0
    if end_index == 0:
        return None,None
    elif ":" in collated_text[prev_end:end_index]:
        span = collated_text[prev_end:end_index].find(":")
        colon_pos = span + prev_end + 1
        return collated_text[colon_pos:end_index],colon_pos
    else:
        index = end_index-1
        start_index = ""
        while index >= 0:
            if re.search("(\s|\n|>)",collated_text[index]):
                index_in = end_index-2
                while collated_text[index_in] not in ["་","།","\n",">"]:
                    index_in-=1
                start_index = index_in+1
                break
            index-=1
        return collated_text[start_index:end_index],start_index

        
def toyaml(dict):
    return yaml.safe_dump(dict, sort_keys=False, allow_unicode=True)

def from_yaml(yml_path):
    return yaml.safe_load(yml_path.read_text(encoding="utf-8"))

def get_default_word_start(collated_text,note):
    start_index = ""
    start,_ = note['span']
    default_option = note['default_clone_option']
    default_start = start-len(default_option)
    if collated_text[default_start-1] == ":":
        start_index = default_start-1
    else:
        start_index = default_start 
    return start_index

def get_text_id_and_vol_num(text_path):
    text_name = text_path.name[:-4]
    map = re.match(r"([A-Z][0-9]+[a-z]?)\_(v[0-9]+)",text_name)
    text_id = map.group(1)
    vol_num = map.group(2)[1:]
    return text_id, vol_num

def check_all_notes(note):
    for _, note_option in note['note_options'].items():
        if note_option == "":
            return False
        elif "!" in note_option:
            return False
    return True  


def  get_prev_note_span(notes, num):
    if num == 0:
        return None, None
    else:
        return notes[num-1]['span']
    
def get_notes_without_context(page):
    note_list = []
    chunks = re.split(r"(\(\d+\) <.+?>)", page)
    for chunk in chunks:
        if re.search(r"(\(\d+\) <.+?>)", chunk):
            note_list.append(chunk)
    return note_list
    
def get_pages(collated_text, vol_num):
    pages = re.split(f"({int(vol_num)}-[0-9]+)", collated_text)
    return pages

def resolve_title_notes(text_path):
    _, vol_num = get_text_id_and_vol_num(text_path)
    collated_text = text_path.read_text(encoding='utf-8')
    new_collated_text = ""
    pages = get_pages(collated_text, vol_num)
    page = pages[0]
    notes_with_context = get_notes(page)
    notes_without_context = get_notes_without_context(page)
    if len(notes_with_context) == len(notes_without_context):
        for num, note_with_context in enumerate(notes_with_context,0):
            title_check = is_title_note(note_with_context)
            if title_check:
                note = notes_without_context[num]
                page = page.replace(f"{note}", "")
        pages[0] = page
        for page_ in pages:
            new_collated_text += page_
    return new_collated_text


def remove_endline(collated_text):
    text = re.sub(r"\n", " ", collated_text)
    return text
    
# def tranfer_endline(source_text_path, target_text):
#     source_text = source_text_path.read_text(encoding='utf-8')
    