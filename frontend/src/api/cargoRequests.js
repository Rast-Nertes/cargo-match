import client from './client'

export function fetchCargoRequests() {
  return client.get('/cargo-requests')
}

export function createCargoRequest(data) {
  return client.post('/cargo-requests', data)
}

export function suggestMatches(requestId) {
  return client.post(`/matching/cargo-request/${requestId}/suggest`)
}
