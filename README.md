# SSL_Rekeying
Automation of SSL Rekeying

Since SSL Rekeying is required every 397 days, this is a script which does the consolidation and deployment of SSL rekeying in a HA Proxy setup.

We have to get the certificates beforehand from the SSL provider (e.g. GoDaddy)

Here, firstly we are consolidating the certificate, bundle and the private key. We are also creating the necessary backups. Finally we are replacing the SSL certificate.
