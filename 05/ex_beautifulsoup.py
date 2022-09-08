from bs4 import BeautifulSoup

contents = '''
<html lang="en">
<head>
<title>Just testing</title>
</head>
<body>
<h1>Just testing</h1>
<div class="block">
<h2>Some links</h2>
<p>Hi there!</p>
<ul id="data">
<li class="blue"><a href="https://example1.com">Example 1</a></li>
<li class="red"><a href="https://example2.com">Example 2</a></li>
<li class="gold"><a href="https://example3.com">Example 3</a></li>
</ul>
</div>
<div class="block">
<h2>Formulario</h2>
<form action="" method="post">
<label for="POST-name">Nombre:</label>
<input id="POST-name" type="text" name="name">
<input type="submit" value="Save">
</form>
</div>
<div class="footer">
This is the footer
<span class="inline"><p>This is span 1</p></span>
<span class="inline"><p>This is span 2</p></span>
<span class="inline"><p>This is span 2</p></span>
</div>
</body>
</html>
'''

soup = BeautifulSoup(contents, features="html.parser")

import ipdb; ipdb.set_trace()
