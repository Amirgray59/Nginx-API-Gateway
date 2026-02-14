import http from "k6/http";
import { check } from "k6";

export const options = {
  vus: 5,
  duration: "30s",
  thresholds: {
    http_req_failed: ['rate<0.01']
  },
};

const BASE = "http://localhost";
const img = open("./test.jpg", "b");

export default function () {

  const data = {
    file: http.file(img, "test.jpg", "image/jpeg"),
  };

  const res = http.post(`${BASE}/assets/images/`, data);


  check(res, {
    "upload success": (r) => r.status === 201,
  });
}
