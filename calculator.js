

function from_gasoline(fuel_type, daily_km) {
    
    var co2PerMile = 404;
    
    var daily_miles = daily_km * 0.62;
    
    var totalCo2;
    
    if (fuel_type == 'Gasoline') {
    
        totalCO2 = daily_miles * 404;
    
    }
    
    return totalCo2*7;
}

function from_meat(lamb, beef, pork, turkey, chicken, fish) {
    
    var meats = [lamb, beef, pork, turkey, chicken, fish, other_meat];
    
    var CO2perGram = [27,39.2,12.1,10.9,6.9,6.1];
    
    var avgMeatServing = 28.35;
    
    var totalCO2 = 0;
    
    for (let i = 0; i < 6; i++) {
        
        totalCO2 = totalCO2 + means[i]*CO2perGram[i]*avgMeatServing;
        
    }
    
    return totalCO2;
}

function from_meat_biproducts(cheese, eggs, milk) {
    
    var bi_products = [cheese, eggs, milk];
    
    var CO2perGram = [13.5, 4.8, 1.0];
    
    var gramsPerServing = [57,63,250];
    
    var totalCO2 = 0;
    
    for (let i=0; i < 3; i++) {
        
        totalCO2 = totalCO2 + bi_products[i]*CO2perGram[i]*gramsPerServing[i];
    
    }
    
    return totalCO2;
}

function other_foods(potatoes, rice, nuts, beansAndTofu, fruit, vegetables, lentils) {
    
    var foods = [potatoes, rice, nuts, beansAndTofu, fruit, vegetables, lentils];
    
    var CO2perGram = [2.9,2.7,2.3,2,2,1.1,0.9];
    
    var gramsPerServing = [236, 90, 30, 57,80, 75,50]
    
    var totalCO2 = 0;
    
    for (let i=0; i < 7; i++) {
        
        totalCO2 = totalCO2 + foods[i]*CO2perGram[i]*gramsPerServing[i];
    
    }
    
    return totalCO2;
}

function power(kWh) {

    var percent_source = {coal: 0.38,gas: 0.23, hydro:0.16, nuclear: 0.10, other_renewable: 0.07, oil:0.03, other:0.03};
    
    var co2PerSource = {coal: 1000, gas: 443, hydro: 10, nuclear:66, other_renewable: 20,oil:778, other:100};   
    
    var totalCO2 = 0;
    
    for (var key in percent_source) {
    
        totalCO2 = totalCO2 + percent_source[key]*co2PerSource[key];
    
    }
    
    return toString(totalCO2*kWh);
    
}

function calculator() {
    
    //call each of the above functions using the use inputted values
    //display the stuff inside the functions, and the total co2
    
    //return a list containing two lists: 1) sorted by amount of co2 emissions 2)a dictionary with the source of emission and amount
    return  ["transportation", "eating meat", "meat bi-products", "power", ""]
}








