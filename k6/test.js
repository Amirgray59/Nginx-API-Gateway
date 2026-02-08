import http from 'k6/http';
import { sleep } from 'k6';

export const options = {

    vus: 20,       // virtual users
    duration: '30s',

    thresholds: {
        http_req_duration: ['p(95)<500'], // SLO → p95 latency < 500ms
        http_req_failed: ['rate<0.01'],   // error rate < 1%
    },
};

export default function () {

    http.get('http://localhost/notes/health');

    sleep(1);
}
