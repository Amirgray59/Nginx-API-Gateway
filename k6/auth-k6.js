import http from "k6/http";
import { check } from "k6";

export const options = {
  vus: 5,
  duration: "30s",
  thresholds: {
    http_req_duration: ["p(95)<500"],
    http_req_failed: ["rate<0.01"],
  },
};

const BASE = "http://localhost";

export default function () {

  const email = `user_${Math.random().toString(36).substring(2)}@example.com`;

  const payload = JSON.stringify({
    email: email,
    password: "StrongPassword123!",
  });

  const params = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const res = http.post(`${BASE}/auth/register`, payload, params);

  check(res, {
    "register status is 200 or 201": (r) =>
      r.status === 200 || r.status === 201,
  });
}
