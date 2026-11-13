# NetworkPro Lab 2 – Flask + Docker (6814951011)

## Screenshots

### 1. Web form
![Web form](screenshots/1-form.png)

### 2. After submitting (message received)
![Message received](screenshots/2-submitted.png)

Second test:

![Form again](screenshots/2b-form-again.png)
![Message received again](screenshots/2c-submitted-again.png)

### 3. Terminal: `docker-compose up` (POST request logged)
![docker-compose up](screenshots/3-docker-compose-up.png)

### 4. Terminal: `log.txt` inside the container
![log.txt in container](screenshots/4-log-txt.png)

```console
$ docker-compose exec web_app cat log.txt
[2026-11-13 11:00:12] Hello from Docker! - Network Programming Chapter 2
[2026-11-13 11:00:12] สวัสดีครับ ทดสอบภาษาไทย
[2026-11-13 11:03:22] hi
[2026-11-13 11:07:57] hi
[2026-11-13 11:13:20] hi hello
[2026-11-13 11:14:32] gg ez
[2026-11-13 11:17:05] ..................
```
The same file, copied out of the container: [log.txt](log.txt)
