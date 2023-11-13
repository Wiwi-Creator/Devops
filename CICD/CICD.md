---
title: 'CICD'
---
CICD
===
## What is CICD ?
---
**CI(Continuous Integration) 持續整合**
- 持續整合是指開發者在完成程式碼後，將其合併到版本控制庫中（EX:Git），然後進行自動化測試。(包括單元測試、集成測試等，以確保新的程式碼與現有程式碼能夠無縫地整合，並且不會引入新的錯誤。)

**CD(Continuous Delivery/Deployment) 持續部署**
- 將測試通過的程式碼交付到環境中，並進行更廣泛的測試，如性能測試、安全測試等。如果一切順利，該程式碼將被部署到生產環境中。這個過程的目的是確保每一個可部署的版本都是高品質、穩定且安全的。

**Why We need it ?**
- 維運角度上來說，自動化部屬及測試，可以在過程中省去大多時間及可能出現錯誤的成本。

**DORA Devops 關鍵四大指標**
- Lead time for changes   - 改版前的閒置時間

    從原始碼交付到成功上線運行的間隔時間
- Deployment frequency    - 部署頻率

    在指定時間內，提交並部署正式上線的Production版本的多寡
- Time to restore service - 服務恢復時間

    從災後停機狀態恢復服務所花的平均時間（MTTR）
- Change failure rate – 改版失敗率

    藉由計算Production(產出版)部署的成敗比值，測量 Production 部署失敗發生的頻率在採取補救措施(EX:Rollback)