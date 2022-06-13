# automated-critical-edition

## Formatting convention

*   ':' are replaced by context
*   No pagination is kept
*   Edition names are written in full form
*   Edition names are italicized

### Mono-syllable words

Input: `གཞན་དག་ལ་ཡང་སླུ་<བསླུ། པེ་ཅིན། སྣར་ཐང་།>མི་མཛད།`

Formatted: `གཞན་དག་ལ་ཡང་སླུ་^1མི་མཛད།` , `^1 སླུ།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Multi-syllable words without ':'

Input: `བདུད་ཀྱི་བུ་མོ་སྒེག་མོ་<པ། པེ་ཅིན། སྣར་ཐང་།>ཡིས`

Formatted: `བདུད་ཀྱི་བུ་མོ་སྒེག་མོ་^1ཡིས` , `^1 སྒེག་པ།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Multi-syllable words with ':'

Input: `རྫུ་འཕྲུལ་:ཙམ་བླང་གི<པེ་ཅིན། སྣར་ཐང་། རྣམ་འཕྲུལ་བ།>། །རྨད་བྱུང་གང་`

Formatted: `རྫུ་འཕྲུལ་ཙམ་བླང་གི^1། །རྨད་བྱུང་གང་` , `^1 རྫུ་འཕྲུལ་རྣམ་འཕྲུལ་བ། _པེ་ཅིན། སྣར་ཐང་།_`

### Multi-syllable words split by marker

Input: `ཐར་པ་རྒྱུད་གཞན་སྐྱེད་<བསྐྱེད། པེ་ཅིན། སྣར་ཐང་།>པ་དང་`

Formatted: `ཐར་པ་རྒྱུད་གཞན་སྐྱེད་པ་^1དང་།` , `^1 བསྐྱེད་པ།` _`པེ་ཅིན། སྣར་ཐང་།`_

### Mid-word addition '+'

Input: `དེ་ལ་བཅོམ་<+ལྡན། པེ་ཅིན། སྣར་ཐང་།>ཞེས་བྱ་བ་ནི་བདུད་བཞི་`

Formatted: `དེ་ལ་བཅོམ་^1ཞེས་བྱ་བ་ནི་བདུད་བཞི་` `^1 བཅོམ་ལྡན།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Full word addition '+'

Input: `རྣམ་པར་རྟོག་ཅིང་ཕུང་པོ་<+ལྔ་པོ། པེ་ཅིན། སྣར་ཐང་།>དེ་དག་ཀྱང་མི་དམིགས་`

Formatted: `རྣམ་པར་རྟོག་ཅིང་ཕུང་པོ་^1དེ་དག་ཀྱང་མི་དམིགས་` `^1 ཕུང་པོ་ལྔ་པོ།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Long addition '+' with '-'

Input: `ཡིན་ཞིང་དེ་གཞན་དང་འདྲེས་པ་ཡང་མ་ཡིན་ནོ། །དེ་བས་ན་(༡) <«པེ་»«སྣར་»-ན།>(༢) <«པེ་»«སྣར་»+ཡན་གར་བ་དག་ཐོས་པའི་ཕྱིར་རོ། །རྗོད་པར་བྱེད་པ་ལ་དབང་པོ་སོ་སོར་ངེས་པའི་ནུས་པ་ཅན་ཡོད་ཀྱི་སྒྲ་ཙམ་དག་ལ་ནི་མ་ཡིན་ནོ། །དེ་ལས་ཐ་དད་ཡོད་དོ་ཞེས། ། འདི་ལ་ཤིན་ཏུ་ཆེས་དད་བྱ། །ཁོ་བོ་ཅག་གིས་ནི།>སྒྲ་ཙམ་གྱི་ངོ་བོ་མ་ལུས་པ་ཅན་`

Formatted: `ཡིན་ཞིང་དེ་གཞན་དང་འདྲེས་པ་ཡང་མ་ཡིན་ནོ། །དེ་བས་ན་^1སྒྲ་ཙམ་གྱི་ངོ་བོ་མ་ལུས་པ་ཅན་` , `^1 དེ་བས་ཡན་གར་བ་དག་ཐོས་པའི་ཕྱིར་རོ། །རྗོད་པར་བྱེད་པ་ལ་དབང་པོ་སོ་སོར་ངེས་པའི་ནུས་པ་ཅན་ཡོད་ཀྱི་སྒྲ་ཙམ་དག་ལ་ནི་མ་ཡིན་ནོ། །དེ་ལས་ཐ་དད་ཡོད་དོ་ཞེས། །འདི་ལ་ཤིན་ཏུ་ཆེས་དད་བྱ། །ཁོ་བོ་ཅག་གིས་ནི།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Omission  '-'

Input: `ཞེས་བྱ་བ་ནི་བདུད་བཞི་<-བཞི། པེ་ཅིན། སྣར་ཐང་།>བཅོམ་པ་སྟེ།`

Formatted: `ཞེས་བྱ་བ་ནི་བདུད་བཞི་བཅོམ་པ་^1སྟེ།` `^1 བདུད་བཅོམ་པ།`_`པེ་ཅིན། སྣར་ཐང་།`_

### Long omission '...' with '-'

Input: `འཇུག་པར་འགྱུར། །:དེ་ལྟར་བདེ་གཤེགས་ཡོན་ཏན་ཚད་མེད་བསམ་མི་ཁྱབ། །མེ་ཏོག་གིས་བརྒྱན་པ་ལས་<«པེ་»«སྣར་»-དེ་ལྟར་བདེ་…….ལས་བདག་གི།>བསོད་ནམས་གང་ཐོབ་པར།`

Formatted: `འཇུག་པར་འགྱུར། །དེ་ལྟར་བདེ་གཤེགས་ཡོན་ཏན་ཚད་མེད་བསམ་མི་ཁྱབ། །མེ་ཏོག་གིས་བརྒྱན་པ་ལས་^1བསོད་ནམས་གང་ཐོབ་པར།` , `^1 དེ་ལྟར་བདེ་ཞེས་པ་ནས་ལས་བདག་གི་ཞེས་པའི་བར་ཆད།`_`པེ་ཅིན། སྣར་ཐང་།`_

Syntax:  , `^1 <2 first words><ཅེས་/ཞེས་/ཤེས་>པ་ནས་<2 last words><ཅེས་/ཞེས་/ཤེས་>པའི་བར་ཆད།`_`པེ་ཅིན། སྣར་ཐང་།`_ (particle suggestion from pybo)

### Long addition '...'

Input: `འདི་སྐད་དུ།<«པེ་»«སྣར་»+མདོར་བསྡུ་ན་དེ་བཞིན་གཤེགས་པའི་..........ས་ལ་བརྟེན་པར་ཞེས་བྱའོ། །(ཞེས་པའི་ཡི་གེ་འདི་རྣམས་ལྡེབ་༡༠༦༩པའི་བསྡུར་མཆན་༡༡པར་དཔེ་བསྡུར་བྱས་ཡོད།)> ཐམས་ཅད་ལ་ནི་།`

Formatted: `འདི་སྐད་དུ།^1 ཐམས་ཅད་ལ་ནི་།` , `^1 text should be found manually`_`པེ་ཅིན། སྣར་ཐང་།`_

## Note selection convention

*   Archaic spellings are removed
*   Notes about the title are removed
*   Sanskrit spellings are not handled
*   Only meaningful notes are kept

## Normalization convention

*   ⚠️ All normalizations are double-checked manually⚠️
*   Normalizations don't appear in notes
*   Archaic spellings are updated
*   Obvious particle errors are corrected
*   Non-word errors are corrected





## Options Ranking

1. First create config file
```bash
cp src/config-example.ini src/config.ini
```

2. Then rank the options

Types of model and their sentence score metric
|Model|Sentence Score Metric|
---|---
LSTM | Probability
RoBERTa | Loss

```python

from rank_options import OptionRanker

ranker = OptionsRanker()

# for config.lm_type = lstm
ranks = ranker.rank(
  options=["འི", "གི", "དི"],
  left_context=["བདེ་ཆེན་", "པདྨ་",  "འཁྱིལ་བ"], # context should be list of words
  right_context=["ཕོ་བྲང་", "ན"]
)

print(ranks)
# [('འི', 1.3756102224075983e-39), ('གི', 3.8162690334265747e-51), ('དི', 7.808966806052166e-57)]

# for config.lm_type = roberta
ranks = ranker.rank(
    options=["འི", "གི", "དི"],
    left_context="བདེ་ཆེན་པདྨ་འཁྱིལ་བ",
    right_context="ཕོ་བྲང་ན"
)
print(ranks)
# [('འི', 5.318869), ('གི', 5.860524), ('དི', 7.019289)]
```