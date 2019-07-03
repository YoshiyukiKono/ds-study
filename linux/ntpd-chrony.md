AWSユーザガイド： Linux インスタンスの時刻の設定

https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/set-time.html

Cloudera(特にKudu？)は、ntpd推奨。

https://github.com/takabow/cloudera-demo-envから引用(bootstrap-common.sh)

```
#Use ntpd instead of chrony
#And Use Amazon Time Sync Service mainly - https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/set-time.html
yum erase -y chrony
yum install -y ntp
cat /etc/ntp.conf
sed -i -e '/^server/d' /etc/ntp.conf
echo "server 169.254.169.123 prefer iburst" >> /etc/ntp.conf
#echo "server time.google.com iburst" >> /etc/ntp.conf
cat /etc/ntp.conf
service ntpd stop
service ntpd start
service ntpd status
chkconfig ntpd on
ntptime
ntpq -p
ntpq -n -c opeers
```
