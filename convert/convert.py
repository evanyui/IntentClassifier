import json, glob
from pprint import pprint

for file in glob.iglob("input/*.json", recursive=True):
    with open(file) as json_data:
        data = json.load(json_data)
        # extract data
        name = data['name'].split('.')[-1]
        userSays = [utterance['data'][0]['text'] for utterance in data['userSays']]
        responses = data['responses'][0]['messages'][0]['speech']
        # create json format
        output = {'name': name, 'userSays': userSays, 'responses': responses}
        # dump json to file
        with open("output/"+name+".json", "w") as out_file:
            json.dump(output, out_file, ensure_ascii=False, indent = 4)

print('Files created in output folder')
            


