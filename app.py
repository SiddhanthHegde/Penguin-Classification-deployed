import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from datetime import date

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    inp_features = []
    features = [x for x in request.form.values()]
    if features[0] == 'Biscoe':
        inp_features.append(0)
    if features[0] == 'Dream':
        inp_features.append(1)
    if features[0] == 'Torgersen':
        inp_features.append(2)
    
    for feature in features[1:7]:
        inp_features.append(float(feature))
    
    d = features[7]
    d = d.split('-')

    inp_features.append(d[2])

    inp_features = np.array(inp_features)
    inp_features = inp_features.reshape(1,8)
    pred = model.predict(inp_features)[0]

    if pred == 0:
        output_text = 'Yo the features match with the Adelie Penguin'
        desc = 'Its scientific whose scientific name is Pygoscelis adeliae. These penguins are mid-sized, being 46 to 71 cm (18 to 28 in) in height and 3.6 to 6.0 kg (7.9 to 13.2 lb) in weight.[5][6] Distinctive marks are the white ring surrounding the eye and the feathers at the base of the bill. These long feathers hide most of the red bill. The tail is a little longer than other penguins tails. The appearance looks somewhat like a tuxedo. They are a little smaller than most other penguin species. Adélie penguins usually swim at around 5 miles per hour (8.0 km/h). They are able to leap some 3 metres (10 ft) out of the water to land on rocks or ice.'
        img_path = '../Adelie Penguins.jpg'
    if pred == 1:
        output_text = 'It looks like this is a Chinstrap penguin'
        desc = 'Its scientific name is Pygoscelis antarcticus. The chinstrap penguin grows to a length of 68–76 cm (27–30 in) and a weight of 3.2–5.3 kg (7.1–11.7 lb), with the weight varying with the time of year. Males are greater in weight and height than females. The adult chinstraps flippers are black with a white edge; the inner sides of the flippers are white. The face is white extending behind the eyes, which are reddish brown; the chin and throat are white, as well, while the short bill is black. The strong legs and the webbed feet are pink. Its short, stumpy legs give it a distinct waddle when it walks. The chinstrap penguin''s black back and white underside provide camouflage in the form of countershading when viewed from above or below, helping to avoid detection by its predators.'
        img_path = '../Chinstrap Penguin.jpg'
    if pred == 2:
        output_text = 'It seems like your penguin is a Gentoo penguin'
        desc = 'whose scientific name is Pygoscelis papua. The gentoo penguin is easily recognized by the wide white stripe extending like a bonnet across the top of its head and its bright orange-red bill. It has pale whitish-pink webbed feet and a fairly long tail – the most prominent tail of all penguin species. Chicks have grey backs with white fronts. As the gentoo penguin waddles along on land, its tail sticks out behind, sweeping from side to side, hence the scientific name Pygoscelis, which means "rump-tailed". Gentoos reach a height of 51 to 90 cm (20 to 35 in), making them the third-largest species of penguin after the emperor penguin and the king penguin. Males have a maximum weight of about 8.5 kg (19 lb) just before molting, and a minimum weight of about 4.9 kg (11 lb) just before mating. For females, the maximum weight is 8.2 kg (18 lb) just before molting, but their weight drops to as little as 4.5 kg (9.9 lb) when guarding the chicks in the nest. Birds from the north are on average 700 g (1.5 lb) heavier and 10 cm (3.9 in) taller than the southern birds. Southern gentoo penguins reach 75–80 cm (30–31 in) in length. They are the fastest underwater swimmers of all penguins, reaching speeds of up to 36 km/h (22 mph). Gentoos are well adapted to extremely cold and harsh climates.'
        img_path = '../gentoo-penguins.jpg'

    return render_template('output.html', prediction_text=output_text, output_image=img_path,description=desc)


if __name__ == "__main__":
    app.run(debug=True)