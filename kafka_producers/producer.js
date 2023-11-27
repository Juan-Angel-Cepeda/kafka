const kafka = require('./client');
const axios = require('axios');
require('dotenv').config();

const makeRequestAllFligths = async () => {
    try{
        const producer = kafka.producer();
        await producer.connect();
        const response = await axios.get(`https://airlabs.co/api/v9/flights?api_key=${process.env.API_KEY}&_fields=lat,lng,dir,alt,flag,airline_iata,aircraft_icao,flight_number&flag=MX`);
        const fligths = [];
        
        response.data.response.forEach((item) => {
            console.log(item);
            fligths.push({
                lat: item.lat,
                lng: item.lng,
                dir: item.dir,
                alt: item.alt,
                flag: item.flag,
                airline_iata: item.airline_iata,
                aircraft_icao: item.aircraft_icao,
                flight_number: item.flight_number
            });
        });
        
        await producer.send({
            topic:'mi-topic',
            messages:[
                {value:JSON.stringify(fligths)},
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
const temporizador = async () =>{
    console.log(time);
    if(time >= 15){
        time = 0;
    }
    time ++;
}
console.log('iniciando');
makeRequestAllFligths();


/*
    kafka-topics --create --topic mi-topic --partitions 1 
    -- replication-factor 1 --bootstrap-server localhost:9091
*/