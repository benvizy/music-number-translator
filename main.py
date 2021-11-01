from flask import *
from flask_bootstrap import Bootstrap
from MusicParser import MusicParser

# Initialize Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# Constants
mp = MusicParser()
scales = ['C', 'F', 'Bt', 'Et', 'At', 'Dt', 'Gt', 'B', 'E', 'A', 'D', 'G']



@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/chodified/<grid_letter>', methods=['GET', 'POST'])
def boxes_one(grid_letter):
    if request.method == 'POST':
        raw_note_data = []
        new_row = []
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

        for row in range(1, 11):
            new_row.append(request.form.get(f'{grid_letter}-chord-{row}'))
            # print(request.form.get(f'chord-{row}'))
            for col in range(1, 30):
                # print(request.form.get(f'num-{row}-{col}'))
                new_row.append(request.form.get(f'{grid_letter}-num-{row}-{col}'))
            raw_note_data.append(new_row)
            new_row = []

        # pprint(raw_note_data)

        for key in scales:
            for row in raw_note_data:
                current_key = mp.rom_to_key(key, row[0])
                new_row = [row[0]]
                print(f'{new_row}--{current_key} in the key of {key}')
                for col in row[1:]:
                    new_note = mp.num_to_note(current_key, col)
                    new_row.append(new_note)
                notes[key].append(new_row)
        # pprint(notes)
        return render_template('results.html', notes=notes)








# This is for testing
if __name__ == '__main__':
    app.run(debug=True)

# This is for the real world!
# Re-Enter Before You Push!
# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0')
