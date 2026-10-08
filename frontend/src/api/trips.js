import client from './client'

export function fetchTrips() {
  return client.get('/trips')
}

export function createTrip(data) {
  return client.post('/trips', data)
}
