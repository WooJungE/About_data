from dash import Dash, html, dcc

markdown_text = '''
# h1 Heading
## h2 Heading
### h3 Heading

***

## Emphasis

**This is bold text**

*This is italic text*

~~Strikethrough~~

## Blockquotes
> Blockquotes

## Lists
Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa

## Code

Inline `code`


``` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
'''

app = Dash(__name__)
app.layout = html.Div([dcc.Markdown(markdown_text)])


if __name__ == '__main__':
    app.run_server(debug=True)

#markdown 형태