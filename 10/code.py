import argparse
from time import time
import json
import statistics

DAY = 10

PUZZLE_TEXT = '''
--- Day 10: Syntax Scoring ---

You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

Syntax error in navigation subsystem on line: all of them
All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.
So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

For example, consider the following navigation subsystem:

[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
Stop at the first incorrect closing character on each corrupted line.

Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
In the above example, an illegal ) was found twice (2*3 = 6 points), an illegal ] was found once (57 points), an illegal } was found once (1197 points), and an illegal > was found once (25137 points). So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?

Your puzzle answer was 389589.

--- Part Two ---

Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

Your puzzle answer was 1190420163.
'''

SAMPLE_INPUT = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

PUZZLE_INPUT = '''
(({({({(({{<{{()<>}}>}}([<[(<>{})(()()))[[{}[]]{<>{}}]>(<(<>[])<[]()>><[{}[]]([]<>)>)]{{({{}[]}{{}{}})}})
[{(<(<<([[[{(([]{})<(){}>)<{<>}(()[])>}]]{[([(()[])[[][]]]<((){})((){})>)({{{}[]}<{}>})]}]){{[[<<{<>}(<
((<[([(({<<<{{<><>}({}<>)}{{<>{}}[[]()]}>>([<[{}{}]>{[()<>]<<>()>}]<(<{}()><[]{}>)<<[]<>>}>)>}[<{<([<><>]<
[<[<({{({{[({[[][]]<{}<>>})<[<{}{}>]([<><>](<>{}))>]{[{[[]{}}{{}{}}}<(<><>)({})>]{({()()}[<>()])
[<{<<({[{{{(<({}()){{}[]}><(<><>)[[]{}]>)}<(([{}{}]{<>[]}))<(<<>[]>){<[]>(<>{})}>>}({{((<>())<
{[([<[<({((([<[]()>{{}()}]<[{}{}]{[]()}>){{<<>[]>}(<<>()>)})([<({}<>)<{}()>>{[()[]]({}[])}]))(([{<
(({[<[((<([[(<[]()>{{}[]})([[]{}]<<><>>)]({{{}()}((){})})]<[<{[]{}}(()<>)>{(()[])<(){}>}]((<()
([<[[((<<({({([]{})<()()>}({()()}([]())))<{(<>[])<()[]>}>}>{{<[[<>()](()<>)](<[]{}><<>()>)
[[{{(<{[[<<{{<()()>(<>())}<{<><>}<<>[]>>}>{<<({}[]){()<>}>([()[]]({}<>})>(({<>()}[[]<>])<{()<>}{<>()}>)}>[[[
<[<{[{{[[(<[{<[]>[[]{}]}<[(){}]<[]<>>)]><[<(<><>)(<>{})>{<<>{}>[[]{}]}]<[[[][]]<<>()>][<<>
<{[<<({[(<[<((()<>)[<><>]){((){})[()[]]}>[{([][]){[]<>)}{[{}[]](<>{})}]]{{{({}[]){()()}}({(){}}{()})}[[{[]
[<([[(<[{<<<<{[]()}<<>{}>><{[]{}}((){})>>>[<<(<>())<{}<>>><({}<>][<>()]>><<[{}[]][<><>]>(<()[]>{{}})>]>}(<<[
(<(<[({([{(<([[]()]<()[]>)[(()())]><({{}[]}<(){}>)[(<>[])(<>[])]>)[<[<<>{}>[{}[]]]<<<>[]>{()()}>>
[{[{<[<(<<<<([()<>]{()<>}){({}[]){{}{}}}>{([[][]]([]()))<<<>{}>{{}[]}>}>{({{[]<>}[<>{}]}[<[]()>((){})]>[([{}
[{{({<<{(<(<(<<><>><<><>>){<{}[]>)>)>)}>>{[<{[<<{(()<>)<{}{}>}{<()()>(()[])}>([<<>[]><()<>>]<[{}{}]<()<>>>)>
<{<{({<{<<<{(({}{})(<>[]))}[([{}()]({}<>))]>[<[<<><>><[]<>>]>]>[[((<[]<>>)[[()[]]<[][]>])<<{{}[
([([(({<<(({{((){})[{}()]}((()()){{}<>})}[[(()())]])(<(((){}){[]()})({{}[]}{{}{}})>{{[<>[]]{[]()}}[[{}<
{[[{[{[{<({[<{[]<>}({}<>)><[<><>]>]<<({}<>)<<>()>>>]<([{<>{}}]<<<>[]><{}()>>){<[()[]][<>{}]>[<<>
<<[<[(<<(<(((<[]<>>){{[]()}(()[])})[<{[][]}(<>())>{<()<>>{()[]}}])(({[[]{}]<{}<>>}(<()<>>[()[]]))<[[
<[<([([([{[<[[<><>]]{([][])[<>{}]}>[{{[][]}{<>()}}(({}[])<[]{}>)]]{<({[]}[()[]])>}}([([(()<>)]{([]{}){{}
{<<[{[{[{(((([<><>](<><>))[<(){}>{<>()}])[{<<>{}>}(<<><>>[()[]])]>({({()<>}({}{}))<[{}[]]{()<>}>}<
{(({((((<[{(<(<>())><([]<>)[{}()]>)[([{}[]]{[][]})[<[]{}>{<>()}]]}<[{{{}<>}[{}[]]}]{<<()>>}>][({(<{}()><{}[]
[([[<<[[{[{<<[{}<>]>(({}())(<>{}))>}]}{{[(({{}{}}[()<>])<(()<>){[]()}>)<<{[]<>}{<>[]}><[[]{}]([][])>>
([<{[(<([{<{[<<><>>[[]()]]<({}<>)[{}{}]>}<<[[]()]{<>{}}><<[][]>[{}()]>>>}{<{<{[]{}}[[]()]>(<
((<<[[<(<[(((<<>{}>(()[]))({[]{}}([]<>)))[{<<>[]><{}[]>}{(<>[]){(){}}}]>[[[[{}<>]<()()>]](<(()<>)(<>)>{[
[(<((<<<[(<<<<[]{}>{()()}>>>{((([]())([]()))){{{[]<>}{<>[]}}{[{}()]{<>()}}}}}]{<<{(([]{}))[<{}<>>({
<<[({[<(<[{(({{}()}{{}<>}))}<<{[[]()][<>{}]}({<>()}<[]<>>)>>][<(<[()<>]>[(<>[])<{}{}>])>[{<[{}{}]([]())>((<>
[{{[<<[<[[({(({}())<<>()>>{{<>}[<><>]}})<<[[<>[]][[]]]({()<>}<()()>)>{{{<><>}}([(){}]<[]>)}>][{<{((){
{[({[[((([{<<<{}{}><()()>><([]{})>><[{()()}{<>{}}]>}][<[<(<>{})(<>{})>((<>{}){{}<>})]<{<[]()>(<>{})}(<
((<{({({({<{<<{}[]>({}{})>[<[]<>>({}[])]}>})})})}({{(<[[([<([]())([][])>][({()()}{{}{}})])[[{
{{{{{[((([({<<<>{}>(()<>)>{[<>[]]{{}()})}[(<[]{}>[<>()])<(()<>)[<>()]>])<({[{}()][()[]]}{[{}<>
{[(([{(<<<[([<{}{}>[{}<>]]<<<>()>[{}()]>)([[<>{}][{}<>]]{{{}()}<<>[]>})]><{{[([]{})[{}[]]]}{({<><
{<{([<[{[{[[[{{}{}}<{}()>]<{{}()}>]]([[([]())[(){}]]<<[]<>>{(){}}>]<[[{}()](()[])]{{()()}}>)}[(<[((
{{{{{[{{(<(((<<>[]>([][])){{()<>}[()<>]})(<{()[]}{<>[]}>({<>()}[(){}])))>)}((<{{<<()[]>(()<>)><<()()>[{
[[[(<[{[{([<<<<>><<>>><[[]{}](()<>)>>]<{[(()<>)[[]<>]]{<[][]>[[]()]>}[<([]<>)[{}{}]>{[(){}]([]
<[<(<{{{{<{[{(()())}[{(){}}{{}()}]]<<[<><>]({})>[(<><>)]>>>({{{(<>[]){()()}}<((){}){()[]}>}({({}()
<[{{[<([[[(<<<()[]>({}())><[{}[]]{[][]}}>)<([{[]()}{{}{}}]{[[]{}][{}<>]})[<<<>{}>><{[]}<<>()>>]>]{
{((<<{[{<[(<[[<><>]{[]<>}][[<>()][{}{}]]>[<{{}()}({}[])>[[<>[]][<>[]]]])<{<({}{})>{<{}<>]{(){}}}
<[{([<<{(([((([]<>))<<{}()>(()[])>)(([()[]]{[]()}))]<[<<{}()><[]{}>><([]<>)<(){}>>][{[<><>][<>
[<(<{[{[[(<{<[<>()]>}([<<>[]>{<><>}]{(()[])(()<>)})>)]((<<(<()<>>{[]{}}){<[]()>}>([<{}<>>([]())
{({[[<<{{[{<{<[]()>}{<{}<>><{}>}>(<{()<>}((){})><{<>{}}([][])>)}][[<{{()()}({}[])}<{<>{}}<<>{}>>>{<<[]()
[{<([<<[{[[<(<<>()><[][]>)>(<<<>{}><{}()>>[[{}<>]<()<>>])]][{([[{}()]]{({}())(()()]})(<<()<>>(()[])>)}<[([[]
[([((([[[(<<{[()<>][{}{}])([<><>]<{}>)>((<{}<>><()<>>)({{}<>}<{}{}>))>[{((()[])[(){}])}({{{}{}
<{[<[[{{<[{([[<><>]]<<{}()>([]<>)>)([(<>[])][({}()){()<>}])}{<([[]<>][<>{}])(<()()>({}[]))>
([{({[({{<((<(()<>){[]{}}><<<>[]><()[]>>)(<{[]<>}[{}[]]><{{}()}[[]()]>))>}}{[[[[<(()())<<>()>
{<<<[<<<{<<{<({}()){[]{}}>}>>}><{<{<[{[][]}(<>)]([[]<>][<><>])>}([{({}[])<{}{}>}]{[[()[]]][[<>[]]<[]{}>]})>}>
[[[(<<(<((([<([]<>)[<>]><([]<>)<{}{}>>]{({{}[]}<()<>>)[<()<>>]}))){{<{<[[][]](<><>)>{<{}{}>{{}[]}}}<[[[]{}]
[[{({[[((((<<(<>{})(()<>)){[<>[]]}>))[(<<<[]<>>{<><>}>>(({{}()}(<>{}))))(<[{[]<>}((){})]{<{}<>>
<<<(([[{{<<({{<><>}<<>{}>})>{[<<<>>[()[]]>[{()[]}{<>[]}]]{{[<><>]}(<{}<>>(<>[]))}}>}}<{<[(({{}{}}{[]()})
{({(({<({[{(<({}<>)[()()]><[<>{}]>){{(()<>){[][]}}([<>()](<>()))}}{[<<{}()>([]{})>[<<>()><<>{}>]][
{<{[(<([[{<({<()[]>[<>[]]}[[<>()]<()()>])>{[[{()<>}{()()}][[{}<>][{}()]]]([{{}<>}]<{<>[]}([])>)}}[<[[<[](
({(<({([{<[[[(<>]({}{})][<()><()[]>]]]<(<[()<>]>{{()[]}[()[]]})([[<>[]][()<>]](({}())([]())))>>}]{(({
{[[<<{[{<[[<((<>[])<{}{}>)>]{<<[(){}]<{}{}>>>[<{()<>}<{}<>>><[()<>]>]}]>><[[({<(<>[]){()<>}>}[[[{}<>]]([[]<>]
<{<<{[{<{([{[[[][]]]}]((<{[]<>}{()}>(<[]{}>[()[]]))<{{()()}[[]{}]}<{<>[]}{<>[]}>]))}<{[([<[][]>
({[({[[[{(<[{(<>())([][])}<([]())({}())}]>({(<()<>>{{}{}})<[()[]]<<>>>}([[{}[]][()]]{{{}[]}<[][]>})))[
[{[{{{([{[({{<[]()>[{}{}]}<{()}<{}<>>>}<[<()[]>{[]()}]>){{{[<>{}][<>[]]}{<()<>>{<>[]}}}[{(<>[])<()[]>}
<<[[{({([([{{(()())<<><>>}}]<(({[]<>})<<(){}><<><>>>)>)(<{{({}[])<[]()>}{({}[])[<>[]]}}>)]<<[<[{()[]}<{}>]
{{[{<(<[<(({<<[]{}]><[[]<>]<<><>>>}<(<(){}>)>)[[([{}{}][[]{}])[<()()>]]<{{{}[]}{{}}}[[[]()]<{}[]>]>])
{<({(<{[[[({(((){})([]()))<(()())([]{})>}[((()()>([][]))])][{[{{{}()}{()()}}[[[]()]{[]<>}]]}{(({[]<>
([{{<<<([<[({<<>[]>{[][]}}(({}{})[<>{}]))]{{((<>{})){<()()>(<>())}}}>]({[([([][])]{[(){}](()[])}){<[{}()}>}
<[{<[<<{[[{[[({}())<{}()>]]([(()<>)][(()())(()[])])}<(<[[][])<()()>>)([[{}](<>[])](<{}()>{[][]
(<([{({{(({{{({}[])}({{}<>}<[]()>)}<<<{}>{()<>}>({<><>}{<>[]})>}({{[<>()][<>[]]}}(<({})<[]()>>)
[{(<[[[<<{{{(([]())([][]))<{()<>}(()<>)>}<[{[]()}[()()]][[[]()][{}()]])}({<(<>()){<><>}>}[[(()()){(){}}]{(<
[(([[{[{((((<<<>()>({}())>{{{}()}[[][]]})<<<{}{}>([])>>)<[{[[]{}]}{<{}{})<{}>}]<(<{}{}>{<>[]}){<[]{}>{
<{<<<((([(<{<<{}[]>[[][]]>[<<><>>]}>)<[[[<()()>{<><>}](<(){}>[[]{}])]][<{{<>()}({}<>)}>{[{<><>)]{(()<>)
(((<(([([[[({<[]>[[][]]}[{<><>}<[]()>])<({[]()}(()[]))>]<[{[{}{}]}(<[]{}><()()>>]<(<()()>)({<><>})>>]<(<
[[{<{({<(((<<{[]()}(()<>)>([{}()][()<>])><[([]<>)[()[]]]{{()()}(<><>)}>){[(<[]>)[[[]{}]{[]()}]]}){[[{<()[
{([{(<{({<((<[()]<()<>>>({{}}[{}<>])))>><{<{<[<>[]]<[]{}>>}<[[{}]({}{})]{(<>())<()()>}>>(<
<[<{{[({{([{{{{}[]}({}<>]}{<[]{}><()[]>}}<[[()][()()]]{{()()}({})}>]{[(<()<>><{}<>>)[[()]{[]{}}]]<{<[]
(<<<[((<[((<[<<>[]>(()<>)]{{[][]}<{}<>>}>[[<{}()>[{}<>]]{{(){}}[{}()]}])<<([{}[]]{(){}})(<[]
({({[<[[{<<([((){}){[]<>}])>({[<()>(<><>)]})>[[({{(){}}}[[<>[]]<[][]>])[<(()())(<><>)>{([])}]]({[([]<>)
<[[[{(([[<[((<<><>>(<>[])}[{<>[]}[<>[]]]){<[<><>]>[(()[])[[]{}]]}](<{<[]<>>(<>[])}((()())<[]<>>)>({<(){}>
[{{{[[{([{{[{(<>())([])}]<(<[]><{}>)>}}{[{[<()[]>{()}][{()<>}{[][]}]}((({}<>)({}()))(<<><>>
[[{[[{{{{{<(<[[]<>]{[]}>)(<<()][()<>]>[{[]()}{<>[]}])>[(<<[]()>{[]<>}>(<[]<>>{<>{}}))[[{<>()}
([[{[[[([(<{[{{}{}}{<>[]}]{{<><>}}}>)<(<{<(){}>[<>[]]}{<{}[]>{{}[]}}>[[({}<>)(()())]<<{}{}><[]()>>
({{{([[({({({{()[]}({}{})}({()<>}[{}<>]))}{{<[{}[]>[[]()]>{[{}()]<[]<>>}}[(<()()><{}{}>)({[]<>}<<><>>)
{{<{{{[{((<[([[]{}]<<>{}>){<<>()>(<>[])}]{{([]()){[]{}}}}><({{{}[]}<[]()>}{<<>[]><[]{}>}>{<[()()](<>
[{([<[<([[[<<(()[]){(){}}>[[{}{}](<><>)]>({[{}()]}<(()<>){()[]}>)]]<<[[(()[])<<>{}>]{<()<>}<{}<>
<[{<({{[([[((<{}>[{}[]])((<>[])([]{})))(([{}[]]{{}()})({{}()}(<>{})))][[(<<>[]>){[{}{}]{[][
<<<<[(({{({([<{}()>{<>[]}](({}<>)<<><>>)){([[]()]{<>{}}){(<><>)}}}){<{[[<>()]]({{}{}}<()()>)}>[[([()](()[]))]
<({[({{{({<{([<>()]){[[]{}]([])}}(<[<>[]][()<>]>([<>[]][<>{}]))>[[((())([]()))<([]<>)((){})>]<
((({[<((<{<([({}{})[{}<>]][<(){}>({}{})])({[[][]]{<><>}}<<<>()><()()>>)>}([[[{<>[]}][{<>[]}
[{[[(((<{<{({(()[]){[]{}}){([]())[<>[]]})[(({}){[]{}})({[]{}}{()()})]}<{({<>{}}){({}<>){()()}}
{(<{[({<(([<<([]{})<(){}>>([{}[]]{{}{}})>]{<{[<>()]{[]<>}}>}))>({{<{<(<>{})([]{})>}<{{()<>}<[][
{(<<[([<[<({([()[]]{<><>})[[<>[]]([][])]}{({[]{}}[[]])(<[]()>)})>]>{<(({[[[]][{}[]]][<{}{}>(()<>)]}<{[{}<>]({
{<({<<{(<{([[<[]<>)[<>[]]](<()[]>)])[[{{()[]}<[][]>}{[()[]][<><>]}][{<{}()>([]<>)}(<<>[]>({}[])
<({[[<{{<[{[<{()<>}>][<[[]<>](<>())>({{}()))]}[((<{}()>([]{}))(([]{})<<><>>))<<{<>{}}[{}[]]>>
{[({[(<([([<[<{}<>>[<><>]]{{<>()}{()()}}><([()<>]<<>()>)({<>[]}({}()))>]<<[[()[]]<<><>>]<((){})(<><
<((({<(<({{{[({}())(()())][(<>)]}[[{{}[]}[<>[]]]([[][]]{()()})]}({{([]{})<[]()>}[(())({}<>)]}<{{[][]}{()()}}
[{{([[([{{{(<<[]()>[()[]]>{{[]<>}[[]()]})[<([]<>)<[][]>>]}}}(([[{(<>{}){[]{}}}{[(){}]{<>[]}}
([[{[{<[([[<[[()[]]([]())]<{<>{}}[<>[]>>>{{(<>())([]<>)}<({}[])<[]{}>>}]{<<{[][]}{<>()}>{(()())<(){}>}><
(<[({<(<(((<[<<>()>{{}()}]{(<>)<()()>}>([(<>[]}<[][]>]{{{}()}(<>)}))[[[{{}[]}{{}}]([[]<>]<{}()>)]])[{<[{[
{<([{(([[[[{((<><>)(<>())){({}())<[]{}>}}<{(<>[]){<>[]}}<{{}<>}[(){}]>>]]][[(<{<{}()>{[]}}[<<>>{{}<>}]>([
<{[[<({[[({([{()()}{[][]}]([[][]]<{}>))}{<[<{}())<[]()>]{(()()){{}<>}}>({[{}<>]{()[]}}<{()<>}
[<<((<(([(<{[[()<>]{{}<>}]([[]()][<>[]])}{(<[]>)((()[]){[]()))}>{{(([][])({}{}))<[(){}]>}})
[<[<{[{{[[[<<((){})<()>><{{}[]}{[]()}>><((()){[][]})>][<{<<>[]>[<>[]]}({<>[]}{()()})><{(<>{})<<>()>}>]][([[
([<[<{<{(((<([{}<>])([<>[]]([][]))>[<([]())<()<>>><<()()>{{}()}>])>[<<<{()<>}<<>[]>>{<{}()
<({{<(<([({<[{<>[]}]<[{}{}]{()[]}>>(({[]()}))}[<<{(){}}([][])>(<()()>{()})>{([[][]]<<>{}>)<<[][]>([]())>}
{[(([<([[<[<{[()]}>[<[<>{}][<><>]>{[()]{<>}}]](<{([][]){[]()}}[{()()}(<>[])]><[[[]<>][[][]]]<
<<({<<<({(<<[<[]()>{[][]}][<{}{}>{[]<>}]>[{{<><>}<()()>}(<{}{}>(<>))]>{[[<()()>[[]()]]{<<>[]><[]{}>}]})
[[[(<<(({[(((((){})(<>{}))<[[]()]{{}{})>)(<[()[]]{[]<>}><[<><>]{<>{}}>))([<({}<>)({}[])>[[(){}]
{[[{<[{([<[<{(<><>)}({{}}([][]))>]{{<[<>{}]>(<<>()>[[]<>])}}>({[<<{}<>><()<>>>(<<>()>{<><>})]}[(<<(
'''

P1_SAMPLE_SOLUTION = 26397

P2_SAMPLE_SOLUTION = 288957

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
        self.p1_scoring = {')': 3,
                        ']': 57,
                        '}': 1197,
                        '>': 25137 }
        self.p2_scoring = {'(': 1,
                        '[': 2,
                        '{': 3,
                        '<': 4 }
        self.matching = { '(': ')',
                         '[': ']',
                         '{': '}',
                         '<': '>'}
        self.corrupt = []
                        
    def p1(self):
        self.p1_solution = 0
        for row in self.input_list:
            this_row = []
            for char in row:
                if char in self.matching:
                    this_row.append(char)
                elif self.matching[this_row[-1]] == char:
                    this_row.pop()
                elif self.matching[this_row[-1]] != char:
                    self.p1_solution += self.p1_scoring[char]
                    self.corrupt.append(row)
                    break
                    
    def p2(self):
        scores = []
        for row in [row for row in self.input_list if row not in self.corrupt]:
            score = 0
            this_row = []
            for char in row:
                if char in self.matching:
                    this_row.append(char)
                elif self.matching[this_row[-1]] == char:
                    this_row.pop()
            this_row.reverse()
            for char in this_row:
                score = (score*5) + self.p2_scoring[char]                
            scores.append(score)
        self.p2_solution = statistics.median(scores)
                
                
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