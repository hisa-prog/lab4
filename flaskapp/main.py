from flask import Flask, jsonify, Blueprint
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

main = Blueprint("/", __name__, template_folder='templates',
                 static_folder='static')


@app.route('/info/<about>/')
def info(about):
    """Example endpoint returning about info    
       This is using docstrings for specifications
    ---
    parameters:
      - name: about
        in: path
        type: string
        enum: ['all','version', 'author', 'year']
        required: true
        default: all
    definitions:
      About:
        type: string
    responses:
      200:
        description: A string
        schema:
          $ref: '#/definitions/About'
        examples:
          versions: '1.0'
    """

    all_info = {
        'all': 'main_author 1.0 2020',
        'version': '1.0',
        'author': 'main_author',
        'year': '2020'
    }

    result = {about: all_info[about]}
    return jsonify(result)


@app.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all', 'rgb', 'cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    all_colors = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)


app.register_blueprint(main, url_prefix='/')
app.run(debug=True)
