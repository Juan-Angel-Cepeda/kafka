const kafka = require('./client');
const axios = require('axios');
require('dotenv').config();

const makeRequestAllFligths = async () => {
    try{
        
        const producer = kafka.producer();
        await producer.connect();
        const response = await axios.get(`https://airlabs.co/api/v9/flights?api_key=${process.env.API_KEY}&_fields=lat,lng,dir,alt,flag,airline_iata,aircraft_icao,flight_number,dep_iata,arr_iata,status&flag=MX`);
        const flights = [];
        
        response.data.response.forEach(item => {
            console.log(item);
            flights.push({
                flight_number: item.flight_number,
                airline_iata: item.airline_iata,
                status: item.status,
                lat: item.lat,
                lon: item.lng,
                dir: item.dir,
                alt: item.alt,
                flag: item.flag,
                aircraft_icao: item.aircraft_icao,
                dep_iata: item.dep_iata,
                arr_iata: item.arr_iata,
            });
        });
        
        await producer.send({
            topic:'mi-topic',
            messages:[
                {value:JSON.stringify(flights)},
            ],
        });
        
        console.log('Informacion enviada');
        await producer.disconnect();   
    
    }
    catch(err){
        console.log(err);
    }
}

let time = 1;
const tempo = async () => {
    console.log(time);
    if(time >= 30){
        time = 0;
    }
    time++;
};

console.log('Iniciando envio de informacion');
setInterval(makeRequestAllFligths, 60000);
setInterval(tempo, 1000);