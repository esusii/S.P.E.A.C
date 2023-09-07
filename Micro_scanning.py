from microdot import Microdot, Response
import urllib.parse

app = Microdot()
Response.default_content_type = 'text/html'

css_style = """
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff;
    margin: 0;
    padding: 0;
}

h1 {
    color: #0d6efd;
    text-align: center;
    padding: 20px;
}

a {
    color: #0d6efd;
    text-decoration: none;
}

button {
    display: block;
    width: 200px;
    height: 50px;
    margin: 20px auto;
    background-color: #0d6efd;
    color: white;
    border: none;
    border-radius: 5px;
}

button:hover {
    background-color: #0b5ed7;
}

.response-box {
    width: 60%;
    margin: 20px auto;
    padding: 20px;
    border-radius: 5px;
    background-color: white;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    text-align: center;
    font-size: 20px;
}
</style>
"""

class ScanningSystem:
    def __init__(self, rows=10, cols=4):
        self.table = [[f'Row {i+1}, Column {j+1}' for j in range(cols)] for i in range(rows)]
        self.current_row = 0
        self.current_column = 0
        self.select_row = True

    def get_next(self):
        if self.select_row:
            self.current_row = (self.current_row + 1) % len(self.table)
            self.select_row = False
        else:
            self.current_column = (self.current_column + 1) % len(self.table[0])
            self.select_row = True
        return self.table[self.current_row][self.current_column]

scanning_system = ScanningSystem()

@app.route('/')
def home(request):
    next_cell = scanning_system.get_next()
    return css_style + f'<h1>{next_cell}</h1>'

@app.route('/select')
def select(request):
    selected_cell = scanning_system.get_next()
    return css_style + f'<h1>Selected: {selected_cell}</h1>'

app.run(debug=True, port=8008)

