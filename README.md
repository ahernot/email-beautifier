# email-beautifier
## v0.1.2

This program adds random styles to an email to make it more fun to read. Enjoy!

To do:
* Add more fonts
* Add random .upper() / .lower() effects (?)
* Separate full-stops and other characters as separators instead of them being part of words
* Split the lines along all line separators!
* Process tabs (\t) and other special characters accurately
* Compute the color gradient manually (in 3D RGB space)







<br><br>
Beacons will apply until closed beacon of same type, or until next beacon of same type (overwrite), or until the document's end.
<br>

Beacons:
* Line spacing:
* Text alignment: `<ta:left>` (do not specify for default, default: `left`); change creates line break '\n'
* Character spacing: `<charspacing:10>` (do not specify for default)



* Vertical alignment: ?

* Font: `<font:font_name>`

* Text size: `<size:size> … </size>` or `<s:size> … </s>`
* Text size gradient: `<size:size_start:size_stop> … </size>` or `<s:size_start:size_stop> … </s>`
<br>
* Text color: `<color:color> … </color>` or `<c:color> … </c>`
* Text color gradient: `<color:color_start:color_stop> … </color>` or `<c:color_start:color_stop> … </c>`
* Background color: `<backgroundcolor:color> … </bc>` or `<bc:color> … </bc>`
* Background color gradient: `<backgroundcolor:color_start:color_stop> … </bc>` or `<bc:color_start:color_stop> … </bc>`
<br>
* Underlined: `<underline> … </underline>` or `<u> … </u>`
* Strikethrough: `<strikethrough> … </strikethrough>` or `<st> … </st>`
* Italicised: `<italics> … </italics>` or `<i> … </i>`
* Bold: `<bold> … </bold>` or `<b> … </b>`
recognised color names: 'blue', 'green', 'red', ... (find what plt can recognise and copy), hex codes