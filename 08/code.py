import argparse
from time import time
import json
import math

DAY = 8

PUZZLE_TEXT = '''
--- Day 8: Seven Segment Search ---

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

Your puzzle answer was 514.

--- Part Two ---

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

Your puzzle answer was 1012272.
'''

SAMPLE_INPUT = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''

PUZZLE_INPUT = '''
cbgefad agc fdega cgdf ecdgfa efgca gaefbd edagbc cg ecafb | cdgafbe cfdg cg gac
gcbdfe cgefb bgadcfe de cfabeg cbgade dbfe ced acfdg egdcf | de bedf ecdgf ecd
dcafgb eagdfb bagdefc abg ba afbc bdgec cdgab gaedfc gadfc | abg ba agfdc gab
agfbe fc fgbadec bdgcef gcdbe fbcead ebgcf cfe gdfc dcbega | edfabc efgab cdfg ecf
fcdeg cfbedg dcfeba fge fcdga ebdg cfebd edgcabf efbagc ge | cbdgef begcaf ge dbcfe
fceadbg ecbg cab cb bdfcea agfce cfaedg gadbf bfagc gceabf | cba cab bc bgce
ecadb dcgea baeg dge fcdga gbdefc abfdgce bcfaed debcga ge | dge egd fdbeac bage
dfc fbgde dgefcb bgfade gbfc cf afecgbd cadge fdegc abcfed | cf cfgb dagec bdegf
edaf bagcdf bafegd efacdbg fbaecg gcbde ad gda bfaeg edbag | dgbafe fcbgae adg dag
fbgdca efacdb faegcbd egbfd acebf feagb ga ecga bgefca gaf | geca gaf gdefacb egac
dcfeab adcfb eac dbgace agdefbc ae decfg caefd feab agfdcb | fgecbad cae bfae eca
befg bcafe begacd ebgfac eba fgeadbc dabgcf bgcaf eb feacd | eafcb agcfb gcbfa facde
acefgdb cbadeg gbcde cde dfbgae eagc dfbeac ec bgade dgcbf | cagfdeb ce gafcbed dgcfb
dafbg cdebg ca cabfge cead fcagbed abcgd febcgd agc egbdac | agc cdebg gac bdgaf
cfbged bfc egfc eadbc fbacgd gfbde dbfce efabdg efdgacb fc | bfegd fbc fcagdb dcefbg
bg fedbcg eadgf edagb dbg fgba dgfeab gafcde aecdb dgfaebc | degfa bdg egabd gbade
cedb fedgbc aedgfb efdgb dagcf cfe ec fdceg caefbg gaebcfd | ec fcgebda dbec dgbfe
bdgeac fbgedca cg bcedg gcb bcefga gacd dfegb adebc ecbdfa | edcagb cgeafbd agcd dgca
fa bfa abcfeg bfgea gdabe defcgb cbgef efca cbedagf fcdgab | fa cegdfb bfecg ecaf
cabfd egbafc bdae dcaef ba gcdfb gcdfae abc bfgdeca daefbc | cfeda eabd gdbcf gcedfa
gbcdafe cfgdab becf bdf edcbaf bf cebagd bdeaf efdag cdaeb | afdeb febc bf fb
gebad caed gcbfde befacg dfgacbe dbcaeg gea ea gbafd dcegb | gbecaf gafceb cbagef caedfgb
adebgf cgafbe agbdc cafbedg dg dcaebg gdb bcadf egabc cgde | ebdgacf cbeadfg fdaegcb bcgdefa
fcbgae gce bgdfec acgf daefbc eacbg bcaef gaebcfd gc aegdb | eafdcb gbaec cgfa fcag
bdfgce ca dcfbae ceafgd dgfca abefcgd dgabf acd aceg gecdf | fabgd cda gacfed dac
gdbfea agcbde abdec dbaefgc fbcae dgeac cdgfae bcdg bd ebd | gcebad adgbef db bd
adcb acgde cde cd baegc edbcgf edacbg gfdea gfabce edgfbac | defbcg dce bfeagdc gbacef
afe agcbfe dgbeac af fcebd afgc aebfc gbadefc egbac gabfed | af ebgcfa af fea
fea cgafbed debga bfgdae fa dgefc aegfd gafb cdafbe dacbeg | af afgde af bcadefg
fcegdab dabcg gdbaec becd de afcdgb abged eabfg fecdag aed | bacdg aed de ade
bd gbd gbecf fbcgd egfdab fagdc bdec fegbdac dfgecb facegb | cedb bdfegc gbdface egcbf
cfagd bdcf bcdgea gcabfe dc cagfbd fdgecba cad bacgf afegd | geacbfd cbdgaf dgbfac cd
gace fdbeca gba cbfae bgdfca efbag dbefacg bcagfe ga fbgde | adcgfbe ga ag cdbafe
fb fgecbda dabecg bfedgc gcfbe ebgdc ecfdab fagce fbe dfbg | fb bfcdeg cdfegb bf
cdge afedbc bgc fdcbg dgfbec ebdfc becdgfa ecfgba cg dgfab | decg bfaedcg fbdag cbfgd
bdafgc gacdf cafgdeb fcdega dfabge edacf fde ed cged bfeac | abdcfeg de abfce bgdeacf
cgfbe de cfebag faedbc gbdfe gbcdfe ecgd def dgbfa dfaegcb | decg ebgfdc ed gbceaf
gfd fcgbd fdgeba df ecdf cdfebg efbcag fbgaecd cgbfe bgdac | gfd efcd gfd dcef
dafe bcaed dbf gfdceb fd agcfb aefbdc beacdg ebfacdg cfbad | fead bdf abefdc defa
bgdce facg fgebad efcda gefcd dcfaeg dabfegc cabfed gfe gf | ecadf dgcaebf gdfabec fg
bcfaed cgeafb cgfedb gcdabef fbecg gacdf facgb abge baf ab | bgae bdgceaf dfcga eagb
degcbf bec aecgdf acdegfb fcbd dgaecb fegab fgdec cb cbefg | gbeaf dfcb gbfdec adcfgeb
cgef cbeafd bgafed ec gefdabc cae deagf caedg cgbda feadgc | ce feabgd ecgad efcg
fgdbae geabcdf ega fdecg ea acbe cbagf cegfa fbagdc aebfcg | ae gea acbe ceab
gabe dcfbae ae dgefc dea cbafgd gebdaf dbgfeca gbadf gefad | ade aed ead adefgb
fabdc cgbdef gdec aecgfb bgfde ebcfd afbdceg ce cef egbafd | cdfbge dgce cabgef ce
ebfacg gdce gbefcd befgd cdabf cfdgb cg efbadg bcg aebgdfc | gbfdc gcb dcge bdcfa
efagc geadfb ca fegcad fca defabc fbgec egfda dgac cbedafg | cdag caf caf dgac
dbaec bd efcda dagcfeb adb cgbea cdgb dacgeb aegcfb baegfd | bda efbcgad cdbg gacbe
ge acbge bedg aeg agfdec cabgd bcdgfa edgcafb egbcad befac | gecba ge fcgdae cdbefag
fdbae gacfde fecbd cgdfeb af gaebcdf aef bfca gaebd cafdbe | aef fea edcgbaf fcbed
dcfg bfagd cdebaf cbaeg fcagdb bdgaef gfacb dfcgbea fac cf | cfbgeda debfga gaecb cf
fbdaec bdfca gd bfgcd gbd bedgca gbefc abdgcf gadf gcdbfae | cdefagb bdg fcabgd dg
ecbgafd ecdgab abedfc eafbgc cabef abd da fcad baedf fgbed | cbeagf dba faecbdg ad
bdefg ecfbd ec cfe aebc fdgeca cbadf cagfedb fbcagd efbcda | ecf ec ec efc
eadfcgb gebdfa afcdb agefd adgbf bgea gb adfecg gfbdce fgb | gbea gbf gcfdeba ageb
cb fegba dfcbgae gefdc gebfc fadbec cbe agfbec adgfbe cbga | daebfc abgc egcdf ebc
dgfec dg bfadcg gacfde eafgcdb agde agcfeb cebdf cafge cgd | bcedf dg dg abdecfg
gbf cagedbf gadf gcbea ebcfda afbcg afdbgc bfgdec adfbc fg | gfb gdfa fdacb fg
bd bfd degaf bedaf gbacfd cfaeb ebdfga fecgda acdgebf bdge | eafcb bd eafdgcb bd
gefba dcagefb gebfad baecf cegbaf fc dacbe fcb egdcbf gcaf | efbga fgca cgadefb dcbefag
edgaf eagfb bfeagc ed cagfbde gdafc egadbc edfb dge gfbead | gabdcef fdage agbfec dfbe
agdbfe gd dbeag acgbedf cdbfag gda cfgeab edfg beacd bgafe | gd efdg gbefa agd
dfgbac efgabd edg afcde bgfda eg abecgfd deagf eagb dbfecg | bedcfg dcbfaeg egd ged
cdfaegb bdcg bcafde deabg dcagef dg badce gfaeb agd edbagc | geabd abced dga dg
faedc bgaec gf cagfe daecbf egcfda fcgd efg cfdbeag bgefad | fecabd afcde gcdf eagdbfc
bcdgfa eabfd cfbde gcbed cbf efbadc gfdabe gbfdeca faec fc | cfb dbgec dbgec feac
fgacb abgefdc feacd bdef dbc db bcedag adecgf acebfd fbdca | cbd cbd bd dfbe
acfdbe daeg gaebfc fga gdcfb dcagbef bfagd ag gdefba badef | ga fadbg agdfb gaf
gbefdc bfegad feag dae gfebd ae dafgbec dfabe daegcb cadfb | daegfb bdagec ea egaf
bcage gefadb cfga fbdecga gdbcef bga aegcbf bdeca gfbec ag | ebacg bedcgfa ebgcdf agb
bdegf dbaegf efabg ag gade fga cedbfg ebfac afcbgd bceafgd | aegfcbd gfdeb bgefdca gaf
efcadgb dfb bgcad fd fdcbg gefcb gfaecb fdec edbgfc aefbgd | df bcdag fbaceg fd
febgcd fgbdcae fdegab cgabf gbfcd gecaf bdcagf cdab bga ba | ba gafdbc gba ab
gefba dafgb gfcae bfde gdceab badgef be afgbced ebg cfgbda | eb eb fcega deabcg
cbfdae egabdfc eacbdg ecdab gce agfbc gaed eg gcfbed egabc | gead dbfgace dgebcfa gade
bacgfd dgfe fdagecb cgebdf fbedc edb eabfc bacdeg fdcgb ed | de ebd dfge debfcga
dcgae ef bgefda dfabec ecdbgfa acdfb efa fadec cbef bacfgd | cfabged acfgebd dfcba eagcdfb
gbfde fcd agcedf cdea edgcf gefbac begdcaf gafec gabdcf dc | dc agfec bgedf bfegac
debgfa cfgba bag fcdgb bcad ba fedcbg afdgbc eafcg cgfdbea | dcagfeb ba ba bfdcgae
bfdgae bdfcage edagbc eagbd febac fgbcad cdeab adc cedg dc | gebdfa edcg ebacf ecgd
cbfdea fcbgade egabd gface bfecga deafcg acegd dc cgdf dca | fcdg fgcd cgfea cgdf
eafcdg cb bedca cdgabfe aefbd gdcea facegb edcabg bac dcbg | cdgb decba gfceda bac
gbdecfa ceabfd edfgb gfba bgdcfe af dgfeba dgaef fae eacgd | dgabfe fa fadeg gbaf
dcaegb gdcfea eadcfb dafcg daecg afd gafe bedcgaf bfcdg af | acdfgbe dfa afd fgea
cfgbdea bfade afecbd faedg bdac aeb fedcb faecbg ba bcgfed | cfdeb egcfdab abe ba
fgcabd geadbcf cdbe ebgdf feacgb cgfeb db gdebcf dgaef bdg | efbgcd gbadfc ebgdfca dgabcf
gebfda ge cbfdega cgde gacfe afecb gef bcgdfa cadegf fdgca | ecdg cedg fcgedba abecf
adebc dbgc abefcd agfde egc gcaebf agecd cg ebafdcg degcab | fgade ceg bgdc gbcd
gacedbf ebgf afegcd beadf cdeba aebfgd fab bgafcd edagf bf | fbge fgcead debac fegb
fcgdeb bgdeca gfeacdb edbga gfea fadbg fg aegfbd fgb fbdac | gf gafe caegdb afcgdbe
cdfeg bd dbfe acdfeg dbfcg dbg afbgc dbgace gdcebf ebcagdf | fcgdb dgb bfcgaed febd
becagf dagefc cdebf gefab dgf gfbde bdegfa dabg gd ecfbgda | gd bfadeg gdf fdg
fcaebg fbadec edgbc fc fagc fec egafb efcbgda fegadb bgecf | fc eabdfg acfg deafbcg
be fbgca fbgade fdgace bcde edbgcf cfgeadb degfc ebf bfceg | cbfdgea bcgaf fcegd gfdeba
cdgba edbgc geca bge gbadce gdfbae dcefb dcfabg gecadfb eg | eg fdbaeg ge geb
cdbfg ad afegcdb ecfba cdfab adec geafbd cfedab dab bgaefc | cbgdafe faebc da ad
edbcf cbgedfa gceb eg gfbad egf gdfbec fabcde bfged gefdac | ebgcdaf ge dgcfeb dbfce
fde fegcba ecdfb acfebd beacf fcdbaeg df afdb bcegd gedfac | gecfba eacfb df cafegbd
edbafgc gd adecb dfga bgdfae bedcfg geafb aegbd gde cebafg | deg gefbcda dgaf edg
gfb eagf cdbfae fg gadbf gdcba dabgef fecgdb dfcaebg afdbe | cabegfd cbdefa gfb bgf
gfa edgfa caefgb gf gbcaed gdcf egcda eabfd edgfac fbecgad | fg fag fg fdcg
gf ebgda cabedgf gcfb cdfbae gef efcab decgfa ecbgfa abfeg | bcgf gf egf gfe
gdae ecfbag badgc ebcfda cbgfd gaefdcb ebgdca ceabg adc da | eacgfb bgadc dca cda
acgbf ceagf cbgafe bfc gbdcfea fdecab bf befg eadcfg dabcg | fdaceb cbf bcf bfge
cedgb bfe efbcg ef acfe fdbacg cdbgeaf gdbaef gebacf cfbga | bagfdc fbceg cafdbg cagebf
dbcgae gfbda ca cbdeg dcgba abfgdec acb efdbgc daec bafegc | agecbd dagcfeb ac ac
bgcfeda gfcba gfe ef degafb eadgb bedf afgbe bdecga gfdace | fe bfde gebaf dceabg
defcba facgeb de cbdea ecfba ebdgaf fecd ade bgfcaed cdbga | dea de acebd ed
bad cgbadfe ecadf ebdcg aedgfb ba aecbd decabg bacg gbfecd | bagc cbag agbc eafdc
cfgde afgeb aec bcfdae gbac abcdegf agdfeb ca gaebfc aegfc | dafgbe eac bgac facegb
gecda eb cbdea cdbfa egadbfc fdecag deabgf bde acdebg gbce | cedagfb gceda facdegb ebd
bgd db fbed fabdg eacdfg dgbecaf cafgb edgfa aebdfg gdaebc | db dfgaec ebdf agdbf
fgecadb abe cagfbd bcdage eb eadgbf dcfea deafb bfeg agdfb | daecgb agfbdec be gbfe
deabg bef caebgfd fdaeb gdebfc fe fcbgda ceaf bacedf bfacd | fe afcgedb eadbf gacbdef
ac gcae aebcd bedcg eadfb bfcged gadcbe acegbfd bac fbacdg | fbgcead cdgbefa dbgcaf bfdcge
egcfa cef cgeab abfc gfedabc abcefg agbdce cf eafgd dbfegc | abcf dafeg fcgbde gaebc
afdceg dgbec egdca bc cedfab ebdfg bacg ebcfagd egacdb bdc | abgc ecgadb abgc dbcaefg
cgefab efcd fcg dfcbge dabgc egbfd bgfcd fc dabegf bedafcg | dgfeb fecd fc cf
dea abcdfge abfecg de edfc ebfac gbcda eagfbd fdaceb daceb | cdgba dbacg badcegf edcf
abgfd fbaegd bfdcga fgbea agcdebf ge gbde cafgde fge ceafb | ebdg gedb cafegd cbdgfa
adbg fecbg caegd bcgead ba aecgdf deabfc cbaeg ceafgbd eba | efgdac becfad fcadbe febcad
cefbag eca cdbeaf dbcefga fbdca dgbcfa efdag decb dfeac ce | cgbaefd ec aefdg cea
bdgfae acgeb cegfd egdca efcdbg dcfa ad gda cgafed cdgabef | ad acedg ad fgdecba
gdfa dcg bcegad gd bfaecg afdcge cedbf cgfae gfedbca fcdeg | gcebda gcd fbedcga cdg
ebafgc da fbdag fgbca bagdfec gdfeb cgfabd dabc egfdca gad | ad badc dagcebf fecdgab
abd bdagfce adfceb adbcf egbfda febgdc da cead acgbf cbedf | bgadef efbcdg da fagbed
bae dfagbe fecba edacfbg baecdf bdec gbdcaf be bdacf agcef | ecfadbg be abegcdf bdec
bcd fegadb gcafebd badgec eadc abdfcg aegbd dc gcedb fcegb | dbc cd abdgcf acgedb
fg bfdeg dfeab dfg cbegfd ceadbg efadgcb cdbge fgce dfgcab | gbafecd gfcbda gfd bdgaec
agcf acb edfgcb fabdcge begad ac dfgcab dgcbf abdgc cebfad | gfedabc badge gacf ebgda
dfgabe fge dbfagc edfca gebc ge badgecf fagec fbgac baecfg | cegfa gfbca fcdbga eg
dagb ebgdf fgbaed ab ecbfadg befga fabcde baf fcega begdcf | gbfcaed afb adbg bgda
dfgec efabcg ebfag cga agbdef beac dgfacb cagdbef ca fgaec | ecbgaf fagce cag bace
ae fgbdea dbcfag cbea begdcaf gea gdecf decga cgdabe bagdc | ae ega bcfagde ae
bgaec efgbadc cgeafb becdga cadbfe bafgc afeg fa bfa fgcbd | fdabegc afb feag gbace
cfbdgea egfabd ed afecg fdaec cdafb cgdafe dae gfebca cged | cagfe cgfbade ed dceagfb
bfegad ecdb acbfg gdb fdcgeb db bdgfc acebdfg cdgef dcfgae | gbd bd cdeb gcefd
dcba cb decfga bagfe gdabecf bdgafc gcdfa bgc ecdfbg abgcf | bc gdaefc fcdeabg fbage
cf efdc cdfgba dcgaef dbegacf fgbea ecgfa ceagbd cfg decag | gedcab cf fedc cf
cg gadcef edabcgf dgfea abefgd ebgdcf acfge cge baefc cdag | gc begfda gc gedaf
bc fcageb cbg cfagd cfgdb agcfed fdebgca dcfbag efgbd bcda | abcfge fgdeac bc bcda
cgabf cf efdacgb cgaeb cefadg bcefga fgc ceagdb ebfc badfg | dbfga gcf gacbf cbegaf
dbg cfbgae dbceg cagd gd gbfdeac cgaeb bfecd agfebd decabg | eacbgfd eadgbf dg agecbd
gebfdc gcabf bdcgfea gcdba fcdgea afbe cafeg bf fbc beagcf | fbae agfbc cbgefad afgcb
fcae baefdgc feadcb cedba fbe fe bagfd bdefcg edafb abedgc | faec dcegba dagceb fgdba
egfbcda ecbfg ebdcgf fcadbg cd ebdc edcgf gafed efbcga gdc | bced bdgcfae dgfec efabgc
geb gfdeac feagc egbfc dbcfgea cebfd fdeagb bcfega bacg bg | abcg cbag bge dacbefg
bcdef afe ecab bcefdg edfca febcad ea cfagd dfbegca dagbef | ea fgdeab afe eaf
acdbegf gbcfda bfge dcefb bgd febadc dcaeg gb degbc gfdecb | fabcdeg aecgd gbd gb
fba cdaefb cbgefd ba afebdg afegb bgacfed fbdeg gbda caegf | ab efdgb bgad dfebg
eaf bcegda fe gacef gefb agcbe cedfbag dagcf defbac afecbg | ef aecfg ebgf gbedafc
fgedb ad fcage dcae cedbafg aegdf dagefc afd gafcdb geacbf | gcaef befagc da dfbgaec
cbdga ecb bcade dgaceb dbeg cbdfag eb fcagbe gebcdfa dface | edbg begd dcbea beadcfg
badfeg af egcdbf deacbf dbacf abgdc dfbagec fba cdfeb afce | cgbad dbgfae fcbad acdefb
ed ced cfaebdg deaf bcgfe bgadec dbafgc dacbf defacb dbfce | afed bgcaefd cgbef gafedcb
gcfba cbdgea aecgdf cdgebf be bec gcbea dbae gacde egbcdfa | agcbf dcgabfe fagbdec ebda
fedbag fagcd dagfe efgc faebgcd egabcd cag badcf fagcde gc | agdfc caedgb gca cg
gbfecad bdafge fgb bfdae eabfdc fgbeac gcdfa bg debg bgdaf | febad fgceab dfcaeb bgf
eb ebd dgcabf gcabde fcedgab aebg cgadb abfdec ebgcd cfdeg | ebgcd cbfgead bfedgca deafbc
ed acdgfb aed gefabd fegcabd gfed bdaegc edbfa bfeca gdfab | aed ade fdgbace fgadb
bg bfecad fbg bedgcf agfdc efdcb cgbdf bceg fgebcad beadgf | bfg bcgfd dcegabf febdac
cd bgfadc befcga bfcga gacd ecfgdb dfabe dfc bfdca fcgbdae | cbagfd cfd cabfdge dcbfga
gae cbfega adbef acebfd geadb dagbc adgefb ge egfd fcgbead | eg fbegacd edgf eg
fdgbaec abfc gebdfc fa afgbe bfceg dbage cebfag gaf egcafd | cfba dageb afebg fcagbed
acfeb ab bdae afb cbfdga fcdae aefcdg ecfgb cdeabf dfgcbea | abf gdabfc dbefac bafdcg
gcadf febgac gfcbed bcgdf gfa dacfe ga ecfagdb cfbgda abdg | agf edfca egcdafb fag
gef cbfeag cafg gcbae edabcg dfaecgb fg dafgeb ecfbg fdceb | cafg fg ebfcag ebcfg
faedbc fb egcdf cagedb bcdfg eacbgfd bdgac bfc gcadbf afgb | fcedbga bdcag fb aebcgfd
afdeb cafeb becgdfa fgce gcabfe fgcab bgcfda ec bdegca bce | gdcfaeb dgbecfa adfgbc bce
dcega fdgaec aegb bdgca gafdecb fcdab cefdgb egbdac bg gbc | bg bcg gbae bage
cabedg aedbf dba gbdeaf gfba decgbf ab gadfbec edcaf egbdf | eafbd gabf fgba ba
gbcda daegfcb efadb fg cgeadb fcbeag agbfd fbg dfgc bfacdg | dabcgfe gcdfba gbcade acgfbed
bgcda gd fagd bdacfge abgec acbfd agdfbc acefbd gdc gbdefc | dg adbcfg beadfcg gbcda
fgbd cbf bcdfag bfgca fb cfgaed abcge cgafd cdfbae bdgceaf | aegcb fcb bcf bf
daebgf cbefdg cdegfa adce ad fdecbag dgcfe gcbaf gda gdacf | cfgba gad da da
cagdfb egcbfda fbadc gdc efcabd cbfgd efgcb dgeabc adfg dg | cgd dbefgac fdgabce agfd
fedcag gadfceb abecfg cgdbe fcedg gafedb fc deagf dcaf cgf | fc fgc cfda fdac
dgcafe befg fec bcgdf ecdba afgbcd ef cefbd aedfgcb bdcgef | cbead gbfe agdcbfe ecf
cedbaf dcbfa cfgedba gdcbf fecbga daec ad fgedab faceb bda | dgaefb cead fecdgba bafdec
bcdef fgebac fdgb fb edcbgf fbc fagdec fcgde abfgcde cebad | bdfaceg fbcdgea fb bdfegc
dcbea fegdba gaedb cbgdef bg egb fagb feagcd dgafe fdabcge | dcaefbg bfga gafb gfdeab
aecgfd debagc dbgfa dab edabgfc cdafg fbca ba gfbde dcbgfa | ab abdegcf ecabgfd ba
cdefbg fcabd cega bdafeg ag begdca bdagc egbcd dgecfba abg | gbfeadc aceg ag egca
gbfcade gecfa fdceag bdefa bcag gb gfb eafbcg dbgfce faegb | gcab gb bfade cefbdg
fe acdbf gbeafd dafgcb afbce dgfbeca dcef efa gcbae dfcbae | afe cgeba ecdf fbeadc
eacd gdc acfdeg begdfac cfdga agefd bcgfa bgefdc fegadb dc | cd cd dabegcf ecfgabd
cde dabfc eagbd abfcdg bedca afdcbe cfeb daegfc cfegdab ec | ce ecd adcfb gaedb
bedacf fc gfedb fecgadb gcdafe degac dfgce cfga cdf cgdeab | gcfed bgfed ebdfg cdf
afdbce gcfadb fg dgcae bagedfc fegca ebfg eafgbc fag abefc | cafbgde gf efadcb fgbe
fgbedac agcbe cegbf cbfdg bcgaed fgebda ef acfe bfe gceafb | egacfdb ef cabfeg ef
adegb bcaedfg deaf fa afb gcefb edbcag efbgad afgbe bagcdf | edbag fba af dgabefc
edgabf aedc fbagc da ecbgdf bdcga agefdcb gad ecdgb cbdega | cbdag ad fgbdcae dbceg
ec gecbfa cagedf fadge fbgeda cbdga cfde eacdg ceg cfgaebd | ecg ec ecfd ec
gcafeb egbdc bdac daceg dbfge bc cdafge ebc cgdeba fabdgce | dgcbea dfcabeg gdfeca cbdaegf
aeb edbgcf ba dbcge adbg cbgeaf bceadg faced cbaegfd deacb | dfeac bea cebgfa ab
fgacb gdeafb fegabdc bfagec cgf dcbaf ecgfad cbeg cg afebg | gfc fagceb cdfgae fcg
gb gdb gbca ecfgbad cdfgbe afcdgb dfbga bfead gcafd feacgd | beafd bdg dgb aefdb
gb caebgd gfcb aegdfcb acfbe edgaf abg bgfea beagcf dcefab | bga dafge agbdefc efabgc
febcga bfgcda afc cbagefd agcd bfecgd ac dfbca cbfgd befad | ac fca afc cdfab
'''

P1_SAMPLE_SOLUTION = 26

P2_SAMPLE_SOLUTION = 61229

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

def is_subset(test_list,test_sublist):
    if test_list and test_sublist: 
        return all(x in test_list for x in test_sublist)
    else:
        return False

def sort_str(string):
    return ''.join(sorted(string))

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')        
        
    def identify_digits(self,digits):
        this_digits = [False, False, False, False, False, False, False, False, False, False]
        this_segment = [True, False, False, False, False, False, False, False]
        while False in this_digits:
            for digit in [sort_str(digit) for digit in digits if digit not in this_digits]:
                match len(digit):
                    case 2: 
                        this_digits[1] = digit
                    case 3: 
                        this_digits[7] = digit
                        this_segment[1] = [segment for segment in digit if segment not in this_digits[1]][0]
                    case 4: 
                        this_digits[4] = digit
                    case 5: 
                        if is_subset(digit, this_digits[1]): 
                            this_digits[3] = digit
                            this_segment[2] = [segment for segment in this_digits[4] if segment not in digit][0]
                            this_segment[7] = [segment for segment in digit if segment not in this_digits[7] and segment not in this_digits[4]][0]
                            this_segment[4] = [segment for segment in digit if segment != this_segment[1] and segment != this_segment[7] and segment not in this_digits[1]][0]
                        elif this_segment[2] and this_segment[2] in digit:
                            this_digits[5] = digit
                        elif this_segment[2] and this_segment[2] not in digit:
                            this_digits[2] = digit
                    case 6: 
                        if this_segment[4] and this_segment[4] not in digit:
                            this_digits[0] = digit
                        elif is_subset(digit, this_digits[4]):
                            this_digits[9] = digit
                        elif this_segment[4] in digit and this_segment[2] in digit:
                            this_digits[6] = digit
                    case 7:
                        this_digits[8] = digit
        return this_digits
            
    def p1(self):
        self.p1_solution = 0
        for row in [ row.split(' | ') for row in self.input_list ]:
            digits, output = row[0].split(' '), row[1].split(' ')
            digits.sort(key=len)
            this_digits = self.identify_digits(digits)
            for digit in output:
                if sort_str(digit) in [this_digits[1],this_digits[4],this_digits[7],this_digits[8]]:
                    self.p1_solution += 1
                

    def p2(self):
        self.p2_solution = 0
        for row in [ row.split(' | ') for row in self.input_list ]:
            reading = ""
            digits, output = row[0].split(' '), row[1].split(' ')
            digits.sort(key=len)
            this_digits = self.identify_digits(digits)
            for digit in output:
                reading += str(this_digits.index(sort_str(digit)))
            self.p2_solution += int(reading)
                

def main():
    parser = argparse.ArgumentParser(description=f'AOC2022 Puzzle Day { DAY }')
    parser.add_argument("-p", "--showpuzzle", help="Display Puzzle Text", action='store_true')
    parser.add_argument("-s", "--showsample", help="Display Sample Input", action='store_true')
    args = parser.parse_args()
    
    if args.showpuzzle:
        print(f"###############\nAOC 2022 DAY {DAY} PUZZLE TEXT\n###############")
        print(PUZZLE_TEXT)
    
    if args.showsample:
        print(f"###############\nAOC 2022 DAY {DAY} SAMPLE INPUT\n###############")
        print(SAMPLE_INPUT.strip())
        print(f"\n###############\nAOC 2022 DAY {DAY} P1 SAMPLE SOLUTION\n###############")
        print(P1_SAMPLE_SOLUTION)
        print(f"\n###############\nAOC 2022 DAY {DAY} P2 SAMPLE SOLUTION\n###############")
        print(P2_SAMPLE_SOLUTION)
    

    if P1_SAMPLE_SOLUTION:            
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=SAMPLE_INPUT)
        sample.p1()
        if P1_SAMPLE_SOLUTION == sample.p1_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P1_SAMPLE_SOLUTION}, got {sample.p1_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle = Puzzle(input_text=PUZZLE_INPUT)
            puzzle.p1()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p1_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
        
    if P2_SAMPLE_SOLUTION:
        print("PART 2\nTesting Sample...\n")
        start_time = time()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle.p2()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()