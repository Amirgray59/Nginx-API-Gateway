
         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 

     execution: local
        script: k6/test.js
        output: -

     scenarios: (100.00%) 1 scenario, 20 max VUs, 1m0s max duration (incl. graceful stop):
              * default: 20 looping VUs for 30s (gracefulStop: 30s)


running (0m01.0s), 20/20 VUs, 0 complete and 0 interrupted iterations
default   [   3% ] 20 VUs  01.0s/30s

running (0m02.0s), 20/20 VUs, 20 complete and 0 interrupted iterations
default   [   7% ] 20 VUs  02.0s/30s

running (0m03.0s), 20/20 VUs, 40 complete and 0 interrupted iterations
default   [  10% ] 20 VUs  03.0s/30s

running (0m04.0s), 20/20 VUs, 60 complete and 0 interrupted iterations
default   [  13% ] 20 VUs  04.0s/30s

running (0m05.0s), 20/20 VUs, 80 complete and 0 interrupted iterations
default   [  17% ] 20 VUs  05.0s/30s

running (0m06.0s), 20/20 VUs, 100 complete and 0 interrupted iterations
default   [  20% ] 20 VUs  06.0s/30s

running (0m07.0s), 20/20 VUs, 120 complete and 0 interrupted iterations
default   [  23% ] 20 VUs  07.0s/30s

running (0m08.0s), 20/20 VUs, 140 complete and 0 interrupted iterations
default   [  27% ] 20 VUs  08.0s/30s

running (0m09.0s), 20/20 VUs, 160 complete and 0 interrupted iterations
default   [  30% ] 20 VUs  09.0s/30s

running (0m10.0s), 20/20 VUs, 180 complete and 0 interrupted iterations
default   [  33% ] 20 VUs  10.0s/30s

running (0m11.0s), 20/20 VUs, 200 complete and 0 interrupted iterations
default   [  37% ] 20 VUs  11.0s/30s

running (0m12.0s), 20/20 VUs, 220 complete and 0 interrupted iterations
default   [  40% ] 20 VUs  12.0s/30s

running (0m13.0s), 20/20 VUs, 240 complete and 0 interrupted iterations
default   [  43% ] 20 VUs  13.0s/30s

running (0m14.0s), 20/20 VUs, 259 complete and 0 interrupted iterations
default   [  47% ] 20 VUs  14.0s/30s

running (0m15.0s), 20/20 VUs, 279 complete and 0 interrupted iterations
default   [  50% ] 20 VUs  15.0s/30s

running (0m16.0s), 20/20 VUs, 299 complete and 0 interrupted iterations
default   [  53% ] 20 VUs  16.0s/30s

running (0m17.0s), 20/20 VUs, 319 complete and 0 interrupted iterations
default   [  57% ] 20 VUs  17.0s/30s

running (0m18.0s), 20/20 VUs, 339 complete and 0 interrupted iterations
default   [  60% ] 20 VUs  18.0s/30s

running (0m19.0s), 20/20 VUs, 359 complete and 0 interrupted iterations
default   [  63% ] 20 VUs  19.0s/30s

running (0m20.0s), 20/20 VUs, 379 complete and 0 interrupted iterations
default   [  67% ] 20 VUs  20.0s/30s

running (0m21.0s), 20/20 VUs, 399 complete and 0 interrupted iterations
default   [  70% ] 20 VUs  21.0s/30s

running (0m22.0s), 20/20 VUs, 419 complete and 0 interrupted iterations
default   [  73% ] 20 VUs  22.0s/30s

running (0m23.0s), 20/20 VUs, 439 complete and 0 interrupted iterations
default   [  77% ] 20 VUs  23.0s/30s

running (0m24.0s), 20/20 VUs, 459 complete and 0 interrupted iterations
default   [  80% ] 20 VUs  24.0s/30s

running (0m25.0s), 20/20 VUs, 479 complete and 0 interrupted iterations
default   [  83% ] 20 VUs  25.0s/30s

running (0m26.0s), 20/20 VUs, 499 complete and 0 interrupted iterations
default   [  87% ] 20 VUs  26.0s/30s

running (0m27.0s), 20/20 VUs, 519 complete and 0 interrupted iterations
default   [  90% ] 20 VUs  27.0s/30s

running (0m28.0s), 20/20 VUs, 539 complete and 0 interrupted iterations
default   [  93% ] 20 VUs  28.0s/30s

running (0m29.0s), 20/20 VUs, 559 complete and 0 interrupted iterations
default   [  97% ] 20 VUs  29.0s/30s

running (0m30.0s), 20/20 VUs, 579 complete and 0 interrupted iterations
default   [ 100% ] 20 VUs  30.0s/30s

running (0m31.0s), 01/20 VUs, 598 complete and 0 interrupted iterations
default ↓ [ 100% ] 20 VUs  30s


  █ THRESHOLDS 

    http_req_duration
    ✓ 'p(95)<500' p(95)=11.07ms

    http_req_failed
    ✓ 'rate<0.01' rate=0.00%


  █ TOTAL RESULTS 

    HTTP
    http_req_duration..............: avg=18.13ms min=750.43µs med=2.12ms max=951.29ms p(90)=3.63ms p(95)=11.07ms
      { expected_response:true }...: avg=18.13ms min=750.43µs med=2.12ms max=951.29ms p(90)=3.63ms p(95)=11.07ms
    http_req_failed................: 0.00%  0 out of 599
    http_reqs......................: 599    19.322934/s

    EXECUTION
    iteration_duration.............: avg=1.01s   min=1s       med=1s     max=1.95s    p(90)=1s     p(95)=1.01s  
    iterations.....................: 599    19.322934/s
    vus............................: 1      min=1        max=20
    vus_max........................: 20     min=20       max=20

    NETWORK
    data_received..................: 101 kB 3.3 kB/s
    data_sent......................: 46 kB  1.5 kB/s




running (0m31.0s), 00/20 VUs, 599 complete and 0 interrupted iterations
default ✓ [ 100% ] 20 VUs  30s
