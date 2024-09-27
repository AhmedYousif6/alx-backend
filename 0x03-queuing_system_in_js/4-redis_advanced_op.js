import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');

  const schools = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };

  for (const [city, value] of Object.entries(schools)) {
    client.hset('HolbertonSchools', city, value, redis.print);
  }
  client.hgetall('HolbertonSchools', (_err, res) => console.log(res));
});
