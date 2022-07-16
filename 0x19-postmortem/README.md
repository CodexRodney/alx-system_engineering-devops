<img src="https://media3.giphy.com/media/3o6wrvdHFbwBrUFenu/giphy.gif?cid=790b7611fbb5b28820e5c4260d57a55f61102eedd9c1e63c&rid=giphy.gif&ct=g" />
#MY FIRST POSTMORTEM
 * Author: Rodney Mwanje
 * Address: rodney002mwanje@gmail.com
 * Year: 2022

### ISSUE SUMMARY
 * On July 1st 2022, starting from 12:02 to 12:20 AM EAT all the requests to the servers returned an error code 502 bad gateway. All users were unable to access data from the servers.
 * The root cause of this was bad cofiguration setting of the haproxy on the load balancer which made all the system go down.

### THE TIMELINE
 * 12:02 AM EAT :- Report received from users for getting error code 502 bad gateway.
 * 12:04 AM EAT :- Error logs were checked by DevOps team.
 * 12:06 AM EAT :- The browsers cache was cleared and request retried
 * 12:10 AM EAT :- Stopped the haproxy service on load balancer
 * 12:11 AM EAT :- Tried restarting the haaproxy service on load balancer
 * 12:15 AM EAT :- Fixed errors on haaproxy configuration file on load balancer
 * 12:17 AM EAT :- Restarted the haproxy service and load balancers
 * 12:20 AM EAT :- All the servers were back online

### ROOT CAUSE AND RESOLUTION
 * The outage was due to improper configuration of the configuration files of haproxy by an engineer who was adding new servers to the back end section. The engineer did not notice the error after configuration due to poor error handling.
 * The DevOps noticed the load balancer was down after checking all the servers were up and running. The haaproxy configuration file was cross checked and the error found.
 * The team was able to fix the error handling programs to detect such kind of errors in future for faster solving of the issue. The haproxy was then restarted together with the load balancer and everything was back to normal

 <img src="https://learn.g2.com/hs-fs/hubfs/plan%20gif%20marketing%20strategy.gif?width=500&name=plan%20gif%20marketing%20strategy.gif"/>

### CORRECTION AND PREVENTATION MEASURES
 After the discussion, the company decided to prevent future attacks by:
  * Improving of the error handling programs to automatically detect and fix the issue
  * Installation of more load balancers to provide an alternative in case of failure of one.
