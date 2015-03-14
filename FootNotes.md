# Footnotes #

Please add here your own comments, links and ideas about footnotes in txt2tags.


---


by Stefano Darchino

Put in txt2tagsrc these lines:

```
%%%% For Footnotes in Lout
%!postproc(lout): \(\( @FootNote {
%!postproc(lout): \)\) }
%%%% For manage Footnotes in HTML
%!postproc(html): \(\( <small>(
%!postproc(html): \)\) )</small>
```

I write the Footnote into the text as ((This is a note)) then with the command
```
txt2tags -t lout nameFile.t2t
```
and
```
lout -Z nameFile.lout > nemaFile.pdf
```
I have a pdf with Footnotes.

And with
```
txt2tags -t html nameFile.t2t
```
a HTML file with (notes) in small characters.