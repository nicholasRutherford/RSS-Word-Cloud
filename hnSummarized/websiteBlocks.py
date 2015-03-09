
HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
  <title>HN Summarized</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="custom.css">
</head>

<body>

<div class="jumbotron">
    <h1 class="text-center">HN Summarized</h1>
</div>
"""

ROW = '<div class="row">'
ROW_END = "</div>\n"

ELEMENT = """
    <div class="col-sm-6">
        <div class="container-fluid">
            <h3 class="text-center">{0}</h3>
            <h5 class="text-center">{1}</h5>
            <blockquote>
                <p>
                    {2}
                </p>
                <footer>
                    <a href ="{3}">Article</a> | <a href="{4}">HN Comments</a>
                </footer>
            </blockquote>
        </div>
    </div>
"""

DATE = """
<div class="=container-fluid">
    <div class="text-center">
        <h2>{0}</h2>
    </div>
</div>
"""

FOOTER = """
</body>
</html>
"""
