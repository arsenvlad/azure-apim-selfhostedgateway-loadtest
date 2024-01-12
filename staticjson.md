# APIM policy to return plain json

## GET staticjson/resource

```xml
<policies>
    <inbound>
        <base />
        <return-response>
            <set-status code="200" />
            <set-header name="Content-Type" exists-action="override">
                <value>application/json</value>
            </set-header>
            <set-body>{"R0UOS":"YI962DC","8GMEDNHLD":"NV808AQ0","GNL":"VPNH","J2YT29JK77D0SMP":"SQZBXT0QIFDRIX","1XP8PFRU1Q22":"E3WXDQ6TX27SF373Y8U3","VJ39VT005JK":null,"G5FTW3DKTV7USHTMA":null,"27YDT77VOBTGPEK8C":null,"4NFX2GG1NFF6C":null,"H9CTM5810VC14ZVD":null,"4W4ZW1YMGLAYTT":true,"R6Z78R":"IRYYS2Z","33A8HI5":true,"ZWH8DLC1O1Y37UPILX00QC":null,"SW7QA97VT":false,"HQ0O":null,"TLHQPN77E92":null,"A0SYBN":null,"JC1AM5L60G":null,"A0EOFH":null,"Z04CGUXGOR":null,"5PU93C5MGOW48R":null,"YDAR5XALPL":"PLZSKF8G3YJGYQYX3JU3C5AX","XBOEW8HFKY":"OFLM"}</set-body>
        </return-response>
    </inbound>
    <backend>
        <base />
    </backend>
    <outbound>
        <base />
    </outbound>
    <on-error>
        <base />
    </on-error>
</policies>
```
