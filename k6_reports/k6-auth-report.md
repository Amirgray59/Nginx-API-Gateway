
         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 

     execution: local
        script: k6/auth-k6.js
        output: -

     scenarios: (100.00%) 1 scenario, 5 max VUs, 1m0s max duration (incl. graceful stop):
              * default: 5 looping VUs for 30s (gracefulStop: 30s)


running (0m01.0s), 5/5 VUs, 20 complete and 0 interrupted iterations
default   [   3% ] 5 VUs  01.0s/30s

running (0m02.0s), 5/5 VUs, 40 complete and 0 interrupted iterations
default   [   7% ] 5 VUs  02.0s/30s

running (0m03.0s), 5/5 VUs, 60 complete and 0 interrupted iterations
default   [  10% ] 5 VUs  03.0s/30s

running (0m04.0s), 5/5 VUs, 80 complete and 0 interrupted iterations
default   [  13% ] 5 VUs  04.0s/30s

running (0m05.0s), 5/5 VUs, 100 complete and 0 interrupted iterations
default   [  17% ] 5 VUs  05.0s/30s

running (0m06.0s), 5/5 VUs, 120 complete and 0 interrupted iterations
default   [  20% ] 5 VUs  06.0s/30s

running (0m07.0s), 5/5 VUs, 140 complete and 0 interrupted iterations
default   [  23% ] 5 VUs  07.0s/30s

running (0m08.0s), 5/5 VUs, 160 complete and 0 interrupted iterations
default   [  27% ] 5 VUs  08.0s/30s

running (0m09.0s), 5/5 VUs, 180 complete and 0 interrupted iterations
default   [  30% ] 5 VUs  09.0s/30s

running (0m10.0s), 5/5 VUs, 200 complete and 0 interrupted iterations
default   [  33% ] 5 VUs  10.0s/30s

running (0m11.0s), 5/5 VUs, 220 complete and 0 interrupted iterations
default   [  37% ] 5 VUs  11.0s/30s

running (0m12.0s), 5/5 VUs, 240 complete and 0 interrupted iterations
default   [  40% ] 5 VUs  12.0s/30s

running (0m13.0s), 5/5 VUs, 260 complete and 0 interrupted iterations
default   [  43% ] 5 VUs  13.0s/30s

running (0m14.0s), 5/5 VUs, 280 complete and 0 interrupted iterations
default   [  47% ] 5 VUs  14.0s/30s

running (0m15.0s), 5/5 VUs, 300 complete and 0 interrupted iterations
default   [  50% ] 5 VUs  15.0s/30s

running (0m16.0s), 5/5 VUs, 320 complete and 0 interrupted iterations
default   [  53% ] 5 VUs  16.0s/30s

running (0m17.0s), 5/5 VUs, 340 complete and 0 interrupted iterations
default   [  57% ] 5 VUs  17.0s/30s

running (0m18.0s), 5/5 VUs, 360 complete and 0 interrupted iterations
default   [  60% ] 5 VUs  18.0s/30s

running (0m19.0s), 5/5 VUs, 380 complete and 0 interrupted iterations
default   [  63% ] 5 VUs  19.0s/30s

running (0m20.0s), 5/5 VUs, 400 complete and 0 interrupted iterations
default   [  67% ] 5 VUs  20.0s/30s

running (0m21.0s), 5/5 VUs, 420 complete and 0 interrupted iterations
default   [  70% ] 5 VUs  21.0s/30s

running (0m22.0s), 5/5 VUs, 440 complete and 0 interrupted iterations
default   [  73% ] 5 VUs  22.0s/30s

running (0m23.0s), 5/5 VUs, 460 complete and 0 interrupted iterations
default   [  77% ] 5 VUs  23.0s/30s

running (0m24.0s), 5/5 VUs, 480 complete and 0 interrupted iterations
default   [  80% ] 5 VUs  24.0s/30s

running (0m25.0s), 5/5 VUs, 500 complete and 0 interrupted iterations
default   [  83% ] 5 VUs  25.0s/30s

running (0m26.0s), 5/5 VUs, 520 complete and 0 interrupted iterations
default   [  87% ] 5 VUs  26.0s/30s

running (0m27.0s), 5/5 VUs, 540 complete and 0 interrupted iterations
default   [  90% ] 5 VUs  27.0s/30s

running (0m28.0s), 5/5 VUs, 560 complete and 0 interrupted iterations
default   [  93% ] 5 VUs  28.0s/30s

running (0m29.0s), 5/5 VUs, 580 complete and 0 interrupted iterations
default   [  97% ] 5 VUs  29.0s/30s

running (0m30.0s), 5/5 VUs, 600 complete and 0 interrupted iterations
default   [ 100% ] 5 VUs  30s


  █ THRESHOLDS 

    http_req_duration
    ✓ 'p(95)<500' p(95)=256.49ms

    http_req_failed
    ✓ 'rate<0.01' rate=0.00%


  █ TOTAL RESULTS 

    checks_total.......: 605     20.020863/s
    checks_succeeded...: 100.00% 605 out of 605
    checks_failed......: 0.00%   0 out of 605

    ✓ register status is 200 or 201

    HTTP
    http_req_duration..............: avg=248.7ms  min=7.84ms med=249.78ms max=261ms    p(90)=254.61ms p(95)=256.49ms
      { expected_response:true }...: avg=248.7ms  min=7.84ms med=249.78ms max=261ms    p(90)=254.61ms p(95)=256.49ms
    http_req_failed................: 0.00%  0 out of 605
    http_reqs......................: 605    20.020863/s

    EXECUTION
    iteration_duration.............: avg=248.86ms min=8.49ms med=249.98ms max=261.17ms p(90)=254.74ms p(95)=256.67ms
    iterations.....................: 605    20.020863/s
    vus............................: 5      min=5        max=5
    vus_max........................: 5      min=5        max=5

    NETWORK
    data_received..................: 105 kB 3.5 kB/s
    data_sent......................: 123 kB 4.1 kB/s




running (0m30.2s), 0/5 VUs, 605 complete and 0 interrupted iterations
default ✓ [ 100% ] 5 VUs  30s
