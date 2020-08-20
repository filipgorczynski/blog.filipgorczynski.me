Title: Przenoszenie linii lub zaznaczonego bloku w górę i w dół w Komodo Edit
Date: 2012-09-08 21:01
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: Komodo, Komodo Edit, przenoszenie bloku, przenoszenie linii
Slug: przenoszenie-linii-lub-zaznaczonego-bloku-w-gore-i-w-dol-w-komodo-edit
Status: published

![Komodo Edit Logo](http://filipgorczynski.files.wordpress.com/2012/09/komodo6.png "komodo6"){.alignleft .wp-image-673 width="102" height="102"}Komodo Edit jako jeden z ciekawszych edytorów pozwala pisać własne makra w językach JavaScript i Python. Mimo ogromnej ilości przydatnych funkcji nie posiada wbudowanego przenoszenia bloków oraz zaznaczenia w górę i w dół. Poniżej makra, które dodają takie działanie do Komodo Edit. Aby wszystko działało jak należy w Views \| Tabs & Sidebars \| Toolbox klikamy prawym przyciskiem myszy i wybieramy Add \> New macro. Podajemy opisowe nazwy, np: Move Line or Move Selection Up, Move Line or Move Selection Down, jako język wybieramy JavaScript i w pole tekstowe wprowadzamy poniższe bloki kodu - otrzymujemy 2 makra. Aby korzystanie było wygodne podpinamy w drugiej zakładce (Key Bindings) skróty klawiaturowe, u mnie Ctrl+Shift+Up oraz Ctrl+Shift+Down.

Przenoszenie linii lub zaznaczonego bloku w dół:

\[code language="javascript"\]  
komodo.assertMacroVersion(3);  
if (komodo.view) { komodo.view.setFocus() };

var ke = komodo.editor;

if( ke.lineFromPosition( ke.currentPos ) == (ke.lineCount - 1) )  
return;

if (ke.selText){

// Extend selection to beg of line at front and end of line at back  
var selStartLine = ke.lineFromPosition(ke.selectionStart);  
var selEndLine = ke.lineFromPosition(ke.selectionEnd);  
var numLinesSelected = selEndLine - selStartLine;

var selStart = ke.positionFromLine(selStartLine);  
var selEnd = ke.getLineEndPosition(selEndLine);

ke.setSel(selStart, selEnd);

// Copy the selected text and remove it  
var text = komodo.interpolate('%s');  
komodo.doCommand('cmd\_delete'); // This leaves a blank line in place of selection

// Move our selection to a new place  
// First move our blank line up  
komodo.doCommand('cmd\_lineNext')  
ke.lineTranspose();

// Insert our text  
ke.insertText(ke.currentPos, text);

// Restore selection  
var newSelStartLine = ke.lineFromPosition( ke.currentPos );  
var newSelEndLine = newSelStartLine + numLinesSelected;

var newSelStart = ke.currentPos;  
var newSelEnd = ke.getLineEndPosition(newSelEndLine);

ke.setSel(newSelStart, newSelEnd);

} else {

komodo.doCommand( 'cmd\_lineNext' );  
ke.lineTranspose();  
}  
\[/code\]

Przenoszenie linii lub zaznaczonego bloku w górę

\[code language="javascript"\]  
komodo.assertMacroVersion(3);  
if (komodo.view) { komodo.view.setFocus() };

var ke = komodo.editor;

if( ke.lineFromPosition( ke.currentPos ) == 0 )  
return;

if (ke.selText){

// Extend selection to beg of line at front and end of line at back  
var selStartLine = ke.lineFromPosition(ke.selectionStart);  
var selEndLine = ke.lineFromPosition(ke.selectionEnd);  
var numLinesSelected = selEndLine - selStartLine;

var selStart = ke.positionFromLine(selStartLine);  
var selEnd = ke.getLineEndPosition(selEndLine);

ke.setSel(selStart, selEnd);

// Copy the selected text and remove it  
var text = komodo.interpolate('%s');  
komodo.doCommand('cmd\_delete'); // This leaves a blank line in place of selection

// Move our selection to a new place  
// First move our blank line up  
ke.lineTranspose();  
komodo.doCommand('cmd\_linePrevious')

// Insert our text  
ke.insertText(ke.currentPos, text);

// Restore selection  
var newSelStartLine = ke.lineFromPosition( ke.currentPos );  
var newSelEndLine = newSelStartLine + numLinesSelected;

var newSelStart = ke.currentPos;  
var newSelEnd = ke.getLineEndPosition(newSelEndLine);

ke.setSel(newSelStart, newSelEnd);

} else {

ke.lineTranspose();  
komodo.doCommand( 'cmd\_linePrevious' );  
}  
\[/code\]

Jeśli dobrze pamiętam to rozwiązanie pochodzi z forum ActiveState dotyczącego Komodo.
