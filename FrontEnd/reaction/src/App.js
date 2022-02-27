import logo from './logo.svg';
import './App.css';
import FormEntry from './FormEntry';
import Legend from './Legend';
import { computeHeadingLevel } from '@testing-library/react';

import { useState } from 'react';

function App() {
  const options = ["Vegetarian Menu Option", "Vegan Menu Option", "Contains Peanuts", "Contains Tree Nuts", "Contains Wheat",
                    "Contains Gluten", "Contains Soy", "Contains Dairy", "Contains Eggs", "Contains Crustacean Shellfish",
                  "Contains Fish", "Halal Menu Option", "Low Carbon Footprint", "High Carbon Footprint",];
  const diningHalls = ["De Neve","Bruin Plate", "Epicuria"];
  const date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
  const month = [1,2,3,4,5,6,7,8,9,10,11,12];
  const meal_period = ["Breakfast","Lunch","Dinner"]
  /* Normal counter variable - DOESN'T WORK
  let counter = 1;
  const increaseCounter = () => {
    counter = counter + 1;
    console.log(counter);
  }
  */

  /*
  // State counter variable
  const [counter, setCounter] = useState(0); // argument = initial value

  const increaseCounter = () => {
    setCounter(
      (prev) =>  {
        let newValue = prev + 1;
        return prev;
      }
    );
  }
  */

  const [diningreturn,  setdiningreturn] = useState([
  ]);


  const sendData = async () => {
    const URL = "http://127.0.0.1:8000/api/";
    // const target = "todos/1";
    const data = {
      month: -1, 
      day: -1,
      year: -1,
      meal: "",
      diningHalls: "",
      filter: "Vegetarian Menu Option"
    }

    let raw = await fetch(URL, 
    {
      method: "POST",
      mode: 'cors',
      headers: new Headers({'content-type': 'application/json'}),
      body: JSON.stringify(data)
    });
    console.log(raw);

    let response = await raw.json();
    console.log(response);

    if (response.length > 0) {
      setdiningreturn(response[0].out);
    }
  }
  const renderMenuItems = diningreturn.map((el) => {
    return (
      <p>{el}</p>
    )
  })
  return (
    <div className="App">
   <h1> Dining Options Selector </h1>

  <Legend options={options} title= "Choose Diet" />
  <Legend options={diningHalls} title= "Choose dining"/>
  <Legend options={date} title= "Day of month (Leave blank if today)"/>
  <Legend options={month} title="Month (Leave blank if today)"/>
  <Legend options={meal_period} title= "Meal Period (Choose One)"/>

    <button onClick={sendData}>Press Me</button>
    <div>
      {renderMenuItems}
      </div>
  </div>
  );
}



export default App;
////////////////////////////////////////////////////////////////////////////////

