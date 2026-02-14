
         /\      Grafana   /‾‾/  
    /\  /  \     |\  __   /  /   
   /  \/    \    | |/ /  /   ‾‾\ 
  /          \   |   (  |  (‾)  |
 / __________ \  |_|\_\  \_____/ 

     execution: local
        script: k6/notes-k6.js
        output: -

     scenarios: (100.00%) 1 scenario, 20 max VUs, 1m0s max duration (incl. graceful stop):
              * default: 20 looping VUs for 30s (gracefulStop: 30s)


running (0m01.0s), 20/20 VUs, 0 complete and 0 interrupted iterations
default   [   3% ] 20 VUs  01.0s/30s

running (0m02.0s), 20/20 VUs, 0 complete and 0 interrupted iterations
default   [   7% ] 20 VUs  02.0s/30s

running (0m03.0s), 20/20 VUs, 0 complete and 0 interrupted iterations
default   [  10% ] 20 VUs  03.0s/30s

running (0m04.0s), 20/20 VUs, 0 complete and 0 interrupted iterations
default   [  13% ] 20 VUs  04.0s/30s

running (0m05.0s), 20/20 VUs, 20 complete and 0 interrupted iterations
default   [  17% ] 20 VUs  05.0s/30s

running (0m06.0s), 20/20 VUs, 21 complete and 0 interrupted iterations
default   [  20% ] 20 VUs  06.0s/30s

running (0m07.0s), 20/20 VUs, 23 complete and 0 interrupted iterations
default   [  23% ] 20 VUs  07.0s/30s

running (0m08.0s), 20/20 VUs, 26 complete and 0 interrupted iterations
default   [  27% ] 20 VUs  08.0s/30s

running (0m09.0s), 20/20 VUs, 35 complete and 0 interrupted iterations
default   [  30% ] 20 VUs  09.0s/30s

running (0m10.0s), 20/20 VUs, 42 complete and 0 interrupted iterations
default   [  33% ] 20 VUs  10.0s/30s

running (0m11.0s), 20/20 VUs, 44 complete and 0 interrupted iterations
default   [  37% ] 20 VUs  11.0s/30s

running (0m12.0s), 20/20 VUs, 48 complete and 0 interrupted iterations
default   [  40% ] 20 VUs  12.0s/30s

running (0m13.0s), 20/20 VUs, 53 complete and 0 interrupted iterations
default   [  43% ] 20 VUs  13.0s/30s

running (0m14.0s), 20/20 VUs, 62 complete and 0 interrupted iterations
default   [  47% ] 20 VUs  14.0s/30s

running (0m15.0s), 20/20 VUs, 65 complete and 0 interrupted iterations
default   [  50% ] 20 VUs  15.0s/30s

running (0m16.0s), 20/20 VUs, 69 complete and 0 interrupted iterations
default   [  53% ] 20 VUs  16.0s/30s

running (0m17.0s), 20/20 VUs, 73 complete and 0 interrupted iterations
default   [  57% ] 20 VUs  17.0s/30s

running (0m18.0s), 20/20 VUs, 81 complete and 0 interrupted iterations
default   [  60% ] 20 VUs  18.0s/30s

running (0m19.0s), 20/20 VUs, 85 complete and 0 interrupted iterations
default   [  63% ] 20 VUs  19.0s/30s

running (0m20.0s), 20/20 VUs, 89 complete and 0 interrupted iterations
default   [  67% ] 20 VUs  20.0s/30s

running (0m21.0s), 20/20 VUs, 93 complete and 0 interrupted iterations
default   [  70% ] 20 VUs  21.0s/30s

running (0m22.0s), 20/20 VUs, 99 complete and 0 interrupted iterations
default   [  73% ] 20 VUs  22.0s/30s

running (0m23.0s), 20/20 VUs, 105 complete and 0 interrupted iterations
default   [  77% ] 20 VUs  23.0s/30s

running (0m24.0s), 20/20 VUs, 110 complete and 0 interrupted iterations
default   [  80% ] 20 VUs  24.0s/30s

running (0m25.0s), 20/20 VUs, 114 complete and 0 interrupted iterations
default   [  83% ] 20 VUs  25.0s/30s

running (0m26.0s), 20/20 VUs, 119 complete and 0 interrupted iterations
default   [  87% ] 20 VUs  26.0s/30s

running (0m27.0s), 20/20 VUs, 125 complete and 0 interrupted iterations
default   [  90% ] 20 VUs  27.0s/30s

running (0m28.0s), 20/20 VUs, 130 complete and 0 interrupted iterations
default   [  93% ] 20 VUs  28.0s/30s

running (0m29.0s), 20/20 VUs, 134 complete and 0 interrupted iterations
default   [  97% ] 20 VUs  29.0s/30s

running (0m30.0s), 20/20 VUs, 140 complete and 0 interrupted iterations
default   [ 100% ] 20 VUs  30.0s/30s

running (0m31.0s), 15/20 VUs, 145 complete and 0 interrupted iterations
default ↓ [ 100% ] 20 VUs  30s

running (0m32.0s), 10/20 VUs, 150 complete and 0 interrupted iterations
default ↓ [ 100% ] 20 VUs  30s


  █ THRESHOLDS 

    http_req_failed
    ✓ 'rate<0.01' rate=0.00%


  █ TOTAL RESULTS 

    checks_total.......: 640     19.416109/s
    checks_succeeded...: 100.00% 640 out of 640
    checks_failed......: 0.00%   0 out of 640

    ✓ create status 200
    ✓ patch ok
    ✓ list ok
    ✓ delete ok

    HTTP
    http_req_duration..............: avg=744.57ms min=2.93ms med=754.29ms max=1s    p(90)=950.15ms p(95)=999.73ms
      { expected_response:true }...: avg=744.57ms min=2.93ms med=754.29ms max=1s    p(90)=950.15ms p(95)=999.73ms
    http_req_failed................: 0.00%  0 out of 640
    http_reqs......................: 640    19.416109/s

    EXECUTION
    iteration_duration.............: avg=3.97s    min=1.35s  med=4s       max=4.95s p(90)=4.35s    p(95)=4.55s   
    iterations.....................: 160    4.854027/s
    vus............................: 10     min=10       max=20
    vus_max........................: 20     min=20       max=20

    NETWORK
    data_received..................: 303 kB 9.2 kB/s
    data_sent......................: 79 kB  2.4 kB/s




running (0m33.0s), 00/20 VUs, 160 complete and 0 interrupted iterations
default ✓ [ 100% ] 20 VUs  30s
