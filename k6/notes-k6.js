import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 20,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01']
  },
};

const BASE = 'http://localhost/notes';

export default function () {

  // create
  let createRes = http.post(`${BASE}/`, JSON.stringify({
    title: "test",
    content: "hello"
  }), {
    headers: { 'Content-Type': 'application/json' }
  });

  check(createRes, {
    'create status 200': (r) => r.status === 200,
  });

  let id = createRes.json().id;

  // update (PATCH)
  let patchRes = http.patch(`${BASE}/${id}`, JSON.stringify({
    title: "updated"
  }), {
    headers: { 'Content-Type': 'application/json' }
  });

  check(patchRes, {
    'patch ok': (r) => r.status === 200,
  });

  // list
  let listRes = http.get(`${BASE}/`);

  check(listRes, {
    'list ok': (r) => r.status === 200,
  });

  // delete
  let deleteRes = http.del(`${BASE}/${id}`);

  check(deleteRes, {
    'delete ok': (r) => r.status === 200 || r.status === 204,
  });

  sleep(1);
}
