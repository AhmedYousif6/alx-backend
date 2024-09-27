import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

async function displaySchoolValue(schoolName) {
  console.log(await promisify(client.get).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};
