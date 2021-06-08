from flask import Flask, render_template, request
import Crawler
import Pairing
import json
import csv

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/search',methods = ['POST', 'GET'])
def result(recurl=None):
    
    if request.method == 'POST':

        with open('initial_data.csv', newline="") as csvfile:
            data_reader = csv.reader(csvfile)
            csv_data = [row for row in data_reader]
            initial_recipe = csv_data[0]
        
        with open('Crawl_data.csv', 'w+',newline='') as f: 
            write = csv.writer(f) 
            write.writerow(initial_recipe)

        return render_template('result.html', result=initial_recipe)

    elif request.method == 'GET':
        temp = request.args.get('recurl')
        temp = str(temp)
        temp = Crawler.Crawler(temp)

        with open('initial_data.csv', 'w+',newline='') as f: 
            write = csv.writer(f) 
            write.writerow(temp)

        return render_template('result.html', result=temp)

@app.route('/pair',methods = ['POST', 'GET'])
def pair():
    if request.method == 'POST':
         
        data = request.form.getlist('category')
        temp_index = int(data[0])

        with open('Crawl_data.csv', newline="") as csvfile:
            data_reader = csv.reader(csvfile)
            csv_data = [row for row in data_reader]
            test_recipe = csv_data[0]

        candiindex = Pairing.replaceIngredient(test_recipe, temp_index)
       
        temp_index = str(temp_index)
        f = open('select_index.csv', 'w+')
        f.write(temp_index)
        f.close()

        return render_template('result.html', result = test_recipe, select_source = candiindex)

    else:
        pass

@app.route('/change',methods = ['POST', 'GET'])
def change():
    if request.method == 'POST':
         
        data = request.form.getlist('pair_source')
        temp_index = data[0]

        with open('Crawl_data.csv', newline="") as csvfile:
            data_reader = csv.reader(csvfile)
            csv_data = [row for row in data_reader]
            test_recipe = csv_data[0]

        f = open('select_index.csv', 'r')
        select_index = f.readlines()
        select_index = int(select_index[0])
        f.close()
        
        
        newrecipe = Pairing.shifting(test_recipe, select_index, temp_index)

        with open('Crawl_data.csv', 'w+',newline='') as f: 
            write = csv.writer(f) 
            write.writerow(newrecipe)
      
        return render_template('result.html', result = newrecipe)
    else:
        pass

@app.route('/result',methods = ['POST', 'GET'])
def final():
    if request.method == 'POST': 
        with open('Crawl_data.csv', newline="") as csvfile:
            data_reader = csv.reader(csvfile)
            csv_data = [row for row in data_reader]
            test_recipe = csv_data[0]
        
        with open('initial_data.csv', newline="") as csvfile:
            data_reader = csv.reader(csvfile)
            csv_data = [row for row in data_reader]
            initial_recipe = csv_data[0]
        
            
        f = open('Crawl_url.csv', 'r')
        Crawl_url = f.readlines()
        f.close()
        Crawl_url = Crawl_url[0]
        return render_template('final.html', result_t = test_recipe, result_i = initial_recipe, url = Crawl_url)
    else:
        pass

if __name__ == '__main__':
    app.run(debug = True)


    