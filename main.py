from flask import *
from flask_bootstrap import Bootstrap
from MusicParser import MusicParser
from pprint import pprint

# Initialize Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Constants
mp = MusicParser()
scales = ['C', 'F', 'Bt', 'Et', 'At', 'Dt', 'Gt', 'B', 'E', 'A', 'D', 'G']



@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        raw_note_data = []
        new_row = []

        for row in range(1,11):
            new_row.append(request.form.get(f'chord-{row}'))
            # print(request.form.get(f'chord-{row}'))
            for col in range(1,30):
                # print(request.form.get(f'num-{row}-{col}'))
                new_row.append(request.form.get(f'num-{row}-{col}'))
            raw_note_data.append(new_row)
            new_row = []

        # pprint(raw_note_data)

        #TODO: Convert Note Data into all different keys!
        notes = {
            'C': [],
            'F': [],
            'Bt': [],
            'Et': [],
            'At': [],
            'Dt': [],
            'Gt': [],
            'B': [],
            'E': [],
            'A': [],
            'D': [],
            'G': [],
        }
        for key in scales:
            for row in raw_note_data:
                current_key = mp.rom_to_key(key, row[0])
                new_row = [row[0]]
                for col in row[1:]:
                    new_note = mp.num_to_note(current_key, col)
                    new_row.append(new_note)
                notes[key].append(new_row)

        # pprint(notes)

        return render_template('results.html', notes=notes)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
