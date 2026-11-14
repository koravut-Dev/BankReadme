<div align="center">

![repo-readme-hyperweave: สกิลอ่าน repo แล้วเขียน README ภาษาไทย](https://hyperweave.app/v1/strip/repo-readme-hyperweave/automata.rimrun?value=OUTPUT%3AREADME.md%2CLANG%3A%E0%B9%84%E0%B8%97%E0%B8%A2%2CDESIGN%3AHyperWeave&variant=teal&pair=violet)

# repo-readme-hyperweave

**สกิลสำหรับ Claude ที่อ่านโค้ดใน repo แล้วเขียน README ภาษาไทยให้ ตามโครงมาตรฐาน มีภาพจาก HyperWeave ที่โหลดได้จริง**

</div>

สั่งว่า "ทำ README ให้ repo นี้" สกิลจะอ่าน manifest, สคริปต์, CI และโครงโฟลเดอร์ก่อน แล้วค่อยเขียน ไม่เดาเองว่าโปรเจกต์ทำอะไร ผลลัพธ์คือไฟล์ `README.md` ที่มีหัวข้อครบตามมาตรฐาน คำสั่งทุกบรรทัดมีอยู่ใน repo จริง และเขียนด้วยภาษาไทยที่คุ้นเคย

## สารบัญ

- [เกี่ยวกับโปรเจกต์](#เกี่ยวกับโปรเจกต์)
- [ฟีเจอร์](#ฟีเจอร์)
- [เริ่มต้นใช้งาน](#เริ่มต้นใช้งาน)
  - [สิ่งที่ต้องมี](#สิ่งที่ต้องมี)
  - [ติดตั้ง](#ติดตั้ง)
- [วิธีใช้](#วิธีใช้)
- [โครงสร้างโปรเจกต์](#โครงสร้างโปรเจกต์)
- [สถาปัตยกรรม](#สถาปัตยกรรม)
- [ทดสอบ](#ทดสอบ)
- [ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ](#ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ)
- [ร่วมพัฒนา](#ร่วมพัฒนา)
- [ใบอนุญาต](#ใบอนุญาต)

## เกี่ยวกับโปรเจกต์

README ที่ AI เขียนมักออกมาเป็นสองแบบ คือแบบเรียบเหมือนกันทุก repo หรือแบบเต็มไปด้วย emoji และคำโฆษณาที่คนอ่านรู้ทันทีว่าไม่ได้เขียนเอง อีกปัญหาคือภาพที่ฝังไว้ บางครั้งลิงก์เสียโดยไม่มีใครรู้ เพราะเซิร์ฟเวอร์ตอบ 200 แต่ส่งภาพ error มาแทน

สกิลนี้แก้ทั้งสามเรื่อง โครงหัวข้อคงที่ตามมาตรฐาน สไตล์ภาพเลือกตามนิสัยโปรเจกต์ และมีสคริปต์ตรวจภาพ โครงสร้าง และสำนวนก่อนส่งงาน

![เส้นคั่น](https://hyperweave.app/v1/divider/dissolve/automata.static)

## ฟีเจอร์

- อ่าน repo แล้วจดข้อเท็จจริงก่อนเขียน เช่น คำสั่งติดตั้งจาก manifest, ตัวแปรจาก `.env.example`, license จากไฟล์ `LICENSE`
- โครงหัวข้อมาตรฐาน 15 หัวข้อ เลือกตามขนาด repo (เล็กมาก ปกติ ใหญ่) หัวข้อที่ repo ไม่มีข้อมูลรองรับจะถูกตัดออก ไม่เติมมั่ว
- ภาพจาก HyperWeave ใช้ลิงก์แบบ stateless ที่เปิดได้จากทุกเครื่อง ไม่ใช้ลิงก์ `/v1/a/` ที่ 404
- เลือกชนิดภาพจากข้อเท็จจริงใน repo: แถบข้อมูล ป้าย ไอคอน การ์ดโปรไฟล์ กราฟดาว ตาราง เส้นคั่น และแผนภาพ 12 แบบ (pipeline, fanout, fanin, hub, dag, tree, lanes, state-machine, sequence, cycle, loop, comparison) พร้อม preset 59 แบบ
- ข้อมูลสดจาก GitHub (ดาว, fork) ใส่เมื่อมี git remote จริงเท่านั้น
- ภาพสว่างและมืดสลับตามธีมของ GitHub ได้
- ห้าม emoji และมีรายการสำนวนที่อ่านแล้วรู้ว่า AI เขียน พร้อมสคริปต์ตรวจ
- ถ้ามี README เดิม จะเก็บไว้เป็น `README.old.md` ก่อนเขียนทับ และถามก่อนส่งชื่อ label ขึ้น hyperweave.app ถ้าเป็น repo ส่วนตัว

สไตล์ที่สกิลเลือกให้เข้ากับโปรเจกต์มี 4 แบบ

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://hyperweave.app/v1/matrix/custom/primer.static?variant=noir&face=dark&spec=eyJ0aXRsZSI6ICLguKrguYTguJXguKXguYwgNCDguYHguJrguJoiLCAic3VidGl0bGUiOiAi4LmA4Lil4Li34Lit4LiB4LmD4Lir4LmJ4LmA4LiC4LmJ4Liy4LiB4Lix4Lia4LiZ4Li04Liq4Lix4Lii4LiC4Lit4LiH4LmC4Lib4Lij4LmA4LiI4LiB4LiV4LmMIiwgImNvbHVtbnMiOiBbeyJpZCI6ICJmaXQiLCAibGFiZWwiOiAi4LmA4Lir4Lih4Liy4Liw4LiB4Lix4LiaIn0sIHsiaWQiOiAibG9vayIsICJsYWJlbCI6ICLguKvguJnguYnguLLguJXguLIifV0sICJyb3dzIjogW3sibGFiZWwiOiAiUGxheWZ1bCIsICJjZWxscyI6IFt7InZhbHVlIjogIuC5geC4reC4myDguYDguIHguKEg4LmE4Lil4Lia4Lij4Liy4Lij4Li1IFVJIOC4h-C4suC4meC4reC4lOC4tOC5gOC4o-C4gSJ9LCB7InZhbHVlIjogImF1dG9tYXRhIOC4hOC4ueC5iOC4quC4tSDguKvguLHguKfguYDguKPguLfguYjguK3guIfguILguKLguLHguJoifV19LCB7ImxhYmVsIjogIkhhY2tlciIsICJjZWxscyI6IFt7InZhbHVlIjogIkNMSSDguYDguITguKPguLfguYjguK3guIfguKHguLfguK3guJnguLHguIHguJ7guLHguJLguJnguLIg4LmC4LiE4Lij4LiH4Liq4Lij4LmJ4Liy4LiH4Lie4Li34LmJ4LiZ4LiQ4Liy4LiZIn0sIHsidmFsdWUiOiAiYnJ1dGFsaXN0IOC5gOC4guC4teC4ouC4pyBjZWxhZG9uIOC5gOC4quC5ieC4meC4p-C4tOC5iOC4h-C4leC4suC4oeC4guC4reC4miJ9XX0sIHsibGFiZWwiOiAiUHJlbWl1bSIsICJjZWxscyI6IFt7InZhbHVlIjogIlNESyDguYHguJ7guKXguJXguJ_guK3guKPguYzguKEg4LiH4Liy4LiZ4LiC4Liy4Lii4Lit4LiH4LiE4LmM4LiB4LijIn0sIHsidmFsdWUiOiAiY2hyb21lIOC5guC4peC4q-C4sCJ9XX0sIHsibGFiZWwiOiAiQ2FsbSIsICJjZWxscyI6IFt7InZhbHVlIjogIuC4o-C4sOC4muC4muC4oOC4suC4ouC5g-C4mSDguYDguK3guIHguKrguLLguKMg4LiH4Liy4LiZ4LiB4Liy4Lij4LmA4LiH4Li04LiZIn0sIHsidmFsdWUiOiAicHJpbWVyIOC4quC4p-C5iOC4suC4hyDguJnguLTguYjguIcifV19XX0">
  <img alt="ตารางสไตล์ 4 แบบ: Playful, Hacker, Premium, Calm และโปรเจกต์ที่เหมาะกับแต่ละแบบ" src="https://hyperweave.app/v1/matrix/custom/primer.static?variant=porcelain&face=light&spec=eyJ0aXRsZSI6ICLguKrguYTguJXguKXguYwgNCDguYHguJrguJoiLCAic3VidGl0bGUiOiAi4LmA4Lil4Li34Lit4LiB4LmD4Lir4LmJ4LmA4LiC4LmJ4Liy4LiB4Lix4Lia4LiZ4Li04Liq4Lix4Lii4LiC4Lit4LiH4LmC4Lib4Lij4LmA4LiI4LiB4LiV4LmMIiwgImNvbHVtbnMiOiBbeyJpZCI6ICJmaXQiLCAibGFiZWwiOiAi4LmA4Lir4Lih4Liy4Liw4LiB4Lix4LiaIn0sIHsiaWQiOiAibG9vayIsICJsYWJlbCI6ICLguKvguJnguYnguLLguJXguLIifV0sICJyb3dzIjogW3sibGFiZWwiOiAiUGxheWZ1bCIsICJjZWxscyI6IFt7InZhbHVlIjogIuC5geC4reC4myDguYDguIHguKEg4LmE4Lil4Lia4Lij4Liy4Lij4Li1IFVJIOC4h-C4suC4meC4reC4lOC4tOC5gOC4o-C4gSJ9LCB7InZhbHVlIjogImF1dG9tYXRhIOC4hOC4ueC5iOC4quC4tSDguKvguLHguKfguYDguKPguLfguYjguK3guIfguILguKLguLHguJoifV19LCB7ImxhYmVsIjogIkhhY2tlciIsICJjZWxscyI6IFt7InZhbHVlIjogIkNMSSDguYDguITguKPguLfguYjguK3guIfguKHguLfguK3guJnguLHguIHguJ7guLHguJLguJnguLIg4LmC4LiE4Lij4LiH4Liq4Lij4LmJ4Liy4LiH4Lie4Li34LmJ4LiZ4LiQ4Liy4LiZIn0sIHsidmFsdWUiOiAiYnJ1dGFsaXN0IOC5gOC4guC4teC4ouC4pyBjZWxhZG9uIOC5gOC4quC5ieC4meC4p-C4tOC5iOC4h-C4leC4suC4oeC4guC4reC4miJ9XX0sIHsibGFiZWwiOiAiUHJlbWl1bSIsICJjZWxscyI6IFt7InZhbHVlIjogIlNESyDguYHguJ7guKXguJXguJ_guK3guKPguYzguKEg4LiH4Liy4LiZ4LiC4Liy4Lii4Lit4LiH4LiE4LmM4LiB4LijIn0sIHsidmFsdWUiOiAiY2hyb21lIOC5guC4peC4q-C4sCJ9XX0sIHsibGFiZWwiOiAiQ2FsbSIsICJjZWxscyI6IFt7InZhbHVlIjogIuC4o-C4sOC4muC4muC4oOC4suC4ouC5g-C4mSDguYDguK3guIHguKrguLLguKMg4LiH4Liy4LiZ4LiB4Liy4Lij4LmA4LiH4Li04LiZIn0sIHsidmFsdWUiOiAicHJpbWVyIOC4quC4p-C5iOC4suC4hyDguJnguLTguYjguIcifV19XX0">
</picture>

### ตัวอย่างภาพที่สกิลทำได้

ทุกภาพข้างล่างเป็นลิงก์จริงที่ผ่าน `check_images.py` แล้ว ตัวเลขดาวและ fork ในแถบแรกมาจาก repo นี้ ส่วนกราฟดาวใช้ repo ของ HyperWeave เป็นตัวอย่างเพราะ repo นี้ยังไม่มีดาวพอจะวาดเส้น

<details open>
<summary>แถบข้อมูล ป้าย ไอคอน การ์ด กราฟ</summary>

<br/>

ข้อมูลสดจาก GitHub (ใช้เมื่อมี git remote จริงและเป็น repo สาธารณะ ค่าที่ดึงไม่ได้จะขึ้น `-` ไม่ใช่เลขปลอม)

<img alt="แถบข้อมูลสดของ repo BankReadme: ดาวและ fork" src="https://hyperweave.app/v1/strip/BankReadme/brutalist.static?data=gh%3Akoravut-Dev%2FBankReadme.stars%2Cgh%3Akoravut-Dev%2FBankReadme.forks&variant=celadon" width="560">

ป้ายสถานะ (ใช้เมื่อมี CI จริง)

<img alt="ป้ายสถานะ CHECKS ผ่าน" src="https://hyperweave.app/v1/badge/CHECKS/passing/primer.static?state=passing&variant=porcelain" width="200">

ไอคอนของเครื่องมือใน stack

<img alt="ไอคอน Python แบบวงกลม" src="https://hyperweave.app/v1/icon/python/primer.static?shape=circle&variant=noir" width="64"> <img alt="ไอคอน GitHub แบบสี่เหลี่ยม" src="https://hyperweave.app/v1/icon/github/primer.static?shape=square&variant=porcelain" width="64">

การ์ดโปรไฟล์ สำหรับ README ของบัญชีบุคคล

<img alt="การ์ดโปรไฟล์ GitHub ของ koravut-Dev" src="https://hyperweave.app/v1/card/koravut-Dev/primer.static?variant=porcelain" width="480">

กราฟประวัติดาว (ตัวอย่างจาก repo ของ HyperWeave)

<img alt="กราฟประวัติดาวของ repo InnerAura/hyperweave" src="https://hyperweave.app/v1/chart/stars/InnerAura/hyperweave/primer.static?variant=porcelain" width="560">

แถบข้อความวิ่ง ใช้เมื่อต้องการจุดที่ขยับจุดเดียวของหน้า

<img alt="แถบข้อความวิ่ง: โครงมาตรฐาน ภาพตรวจแล้ว ภาษาไทย" src="https://hyperweave.app/v1/marquee/BankReadme/brutalist.static?data=text%3A%E0%B9%82%E0%B8%84%E0%B8%A3%E0%B8%87%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%90%E0%B8%B2%E0%B8%99%2Ctext%3A%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B9%81%E0%B8%A5%E0%B9%89%E0%B8%A7%2Ctext%3A%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B9%84%E0%B8%97%E0%B8%A2" width="560">

</details>

<details open>
<summary>เส้นคั่นของแต่ละธีม</summary>

<br/>

| ชื่อ | ตัวอย่าง |
|---|---|
| `aura (primer)` | <img alt="เส้นคั่น aura (primer)" src="https://hyperweave.app/v1/divider/aura/primer.static?variant=porcelain" width="100%"> |
| `seam (brutalist)` | <img alt="เส้นคั่น seam (brutalist)" src="https://hyperweave.app/v1/divider/seam/brutalist.static" width="100%"> |
| `sigil (brutalist)` | <img alt="เส้นคั่น sigil (brutalist)" src="https://hyperweave.app/v1/divider/sigil/brutalist.static" width="100%"> |
| `band (chrome)` | <img alt="เส้นคั่น band (chrome)" src="https://hyperweave.app/v1/divider/band/chrome.static" width="100%"> |
| `current (ใช้ได้ทุกธีม)` | <img alt="เส้นคั่น current (ใช้ได้ทุกธีม)" src="https://hyperweave.app/a/inneraura/dividers/current" width="100%"> |

</details>

<details open>
<summary>แผนภาพ 8 แบบ กับ preset 2 แบบ</summary>

<br/>

| | |
|---|---|
| **วนซ้ำ**<br/>วงจรแก้งานที่วนจนผ่าน<br/><img alt="แผนภาพ วนซ้ำ: วงจรแก้งานที่วนจนผ่าน" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJjeWNsZSIsICJ0aXRsZSI6ICLguKPguK3guJrguYHguIHguYkgUkVBRE1FIiwgIm5vZGVzIjogW3siaWQiOiAiYSIsICJsYWJlbCI6ICLguYDguILguLXguKLguJkiLCAiZGVzYyI6ICIifSwgeyJpZCI6ICJiIiwgImxhYmVsIjogIuC4o-C4seC4meC4leC4o-C4p-C4iCIsICJkZXNjIjogIiJ9LCB7ImlkIjogImMiLCAibGFiZWwiOiAi4LmB4LiB4LmJIiwgImRlc2MiOiAiIn1dLCAiZWRnZXMiOiBbeyJzb3VyY2UiOiAiYSIsICJ0YXJnZXQiOiAiYiJ9LCB7InNvdXJjZSI6ICJiIiwgInRhcmdldCI6ICJjIn0sIHsic291cmNlIjogImMiLCAidGFyZ2V0IjogImEifV0sICJvcmllbnRhdGlvbiI6ICJyaW5nIn0" width="100%"> | **เทียบสอง**<br/>ของเดิมกับของใหม่<br/><img alt="แผนภาพ เทียบสอง: ของเดิมกับของใหม่" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJjb21wYXJpc29uIiwgInRpdGxlIjogIlJFQURNRSDguYDguJTguLTguKHguIHguLHguJrguYPguKvguKHguYgiLCAibm9kZXMiOiBbeyJpZCI6ICJhIiwgImxhYmVsIjogIuC5gOC4lOC4tOC4oSIsICJkZXNjIjogIuC5hOC4oeC5iOC4oeC4tSBIMSDguYTguKHguYjguKHguLXguKrguLLguKPguJrguLHguI0ifSwgeyJpZCI6ICJiIiwgImxhYmVsIjogIuC5g-C4q-C4oeC5iCIsICJkZXNjIjogIuC4q-C4seC4p-C4guC5ieC4reC4oeC4suC4leC4o-C4kOC4suC4meC4hOC4o-C4miJ9XSwgImVkZ2VzIjogW3sic291cmNlIjogImEiLCAidGFyZ2V0IjogImIifV19" width="100%"> |
| **ศูนย์กลาง**<br/>สิ่งที่ทุกอย่างต่อเข้าหา<br/><img alt="แผนภาพ ศูนย์กลาง: สิ่งที่ทุกอย่างต่อเข้าหา" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJodWIiLCAidGl0bGUiOiAiUkVBRE1FIOC4oeC4teC4reC4sOC5hOC4o-C4muC5ieC4suC4hyIsICJub2RlcyI6IFt7ImlkIjogImgiLCAibGFiZWwiOiAiUkVBRE1FIiwgImRlc2MiOiAi4Lio4Li54LiZ4Lii4LmM4LiB4Lil4Liy4LiHIn0sIHsiaWQiOiAiYSIsICJsYWJlbCI6ICLguJXguLTguJTguJXguLHguYnguIciLCAiZGVzYyI6ICIifSwgeyJpZCI6ICJiIiwgImxhYmVsIjogIuC4p-C4tOC4mOC4teC5g-C4iuC5iSIsICJkZXNjIjogIiJ9LCB7ImlkIjogImMiLCAibGFiZWwiOiAi4LmD4Lia4Lit4LiZ4Li44LiN4Liy4LiVIiwgImRlc2MiOiAiIn1dLCAiZWRnZXMiOiBbeyJzb3VyY2UiOiAiaCIsICJ0YXJnZXQiOiAiYSJ9LCB7InNvdXJjZSI6ICJoIiwgInRhcmdldCI6ICJiIn0sIHsic291cmNlIjogImgiLCAidGFyZ2V0IjogImMifV19" width="100%"> | **ต้นไม้**<br/>โฟลเดอร์หรือแพ็กเกจ<br/><img alt="แผนภาพ ต้นไม้: โฟลเดอร์หรือแพ็กเกจ" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJ0cmVlIiwgInRpdGxlIjogIuC5guC4hOC4o-C4h-C4quC4geC4tOC4pSIsICJub2RlcyI6IFt7ImlkIjogInIiLCAibGFiZWwiOiAi4Liq4LiB4Li04LilIiwgImRlc2MiOiAiIn0sIHsiaWQiOiAiYSIsICJsYWJlbCI6ICJyZWZlcmVuY2VzIiwgImRlc2MiOiAiIn0sIHsiaWQiOiAiYiIsICJsYWJlbCI6ICJzY3JpcHRzIiwgImRlc2MiOiAiIn0sIHsiaWQiOiAiYyIsICJsYWJlbCI6ICJldmFscyIsICJkZXNjIjogIiJ9XSwgImVkZ2VzIjogW3sic291cmNlIjogInIiLCAidGFyZ2V0IjogImEifSwgeyJzb3VyY2UiOiAiciIsICJ0YXJnZXQiOiAiYiJ9LCB7InNvdXJjZSI6ICJyIiwgInRhcmdldCI6ICJjIn1dfQ" width="100%"> |
| **ลำดับเรียกกัน**<br/>ใครเรียกใครก่อนหลัง<br/><img alt="แผนภาพ ลำดับเรียกกัน: ใครเรียกใครก่อนหลัง" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJzZXF1ZW5jZSIsICJ0aXRsZSI6ICLguKXguLPguJTguLHguJrguIHguLLguKPguJfguLPguIfguLLguJkiLCAibm9kZXMiOiBbeyJpZCI6ICJ1IiwgImxhYmVsIjogIuC4nOC4ueC5ieC5g-C4iuC5iSIsICJkZXNjIjogIiJ9LCB7ImlkIjogInMiLCAibGFiZWwiOiAi4Liq4LiB4Li04LilIiwgImRlc2MiOiAiIn0sIHsiaWQiOiAidyIsICJsYWJlbCI6ICJoeXBlcndlYXZlLmFwcCIsICJkZXNjIjogIiJ9XSwgImVkZ2VzIjogW3sic291cmNlIjogInUiLCAidGFyZ2V0IjogInMiLCAibGFiZWwiOiAi4Liq4Lix4LmI4LiHIn0sIHsic291cmNlIjogInMiLCAidGFyZ2V0IjogInciLCAibGFiZWwiOiAi4LiC4Lit4Lig4Liy4LieIn0sIHsic291cmNlIjogInciLCAidGFyZ2V0IjogInMiLCAibGFiZWwiOiAi4Lig4Liy4LieIn0sIHsic291cmNlIjogInMiLCAidGFyZ2V0IjogInUiLCAibGFiZWwiOiAiUkVBRE1FIn1dfQ" width="100%"> | **สถานะ**<br/>ค่าสถานะและการเปลี่ยน<br/><img alt="แผนภาพ สถานะ: ค่าสถานะและการเปลี่ยน" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJzdGF0ZS1tYWNoaW5lIiwgInRpdGxlIjogIuC4quC4luC4suC4meC4sOC4guC4reC4hyBSRUFETUUiLCAibm9kZXMiOiBbeyJpZCI6ICJhIiwgImxhYmVsIjogIuC4o-C5iOC4suC4hyIsICJkZXNjIjogIiJ9LCB7ImlkIjogImIiLCAibGFiZWwiOiAi4LiV4Lij4Lin4LiIIiwgImRlc2MiOiAiIn0sIHsiaWQiOiAiYyIsICJsYWJlbCI6ICLguYDguKrguKPguYfguIgiLCAiZGVzYyI6ICIifV0sICJlZGdlcyI6IFt7InNvdXJjZSI6ICJhIiwgInRhcmdldCI6ICJiIn0sIHsic291cmNlIjogImIiLCAidGFyZ2V0IjogImEifSwgeyJzb3VyY2UiOiAiYiIsICJ0YXJnZXQiOiAiYyJ9XX0" width="100%"> |
| **เลนความรับผิดชอบ**<br/>ใครรับผิดชอบขั้นไหน<br/><img alt="แผนภาพ เลนความรับผิดชอบ: ใครรับผิดชอบขั้นไหน" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJsYW5lcyIsICJ0aXRsZSI6ICLguYPguITguKPguJfguLPguK3guLDguYTguKMiLCAibm9kZXMiOiBbeyJpZCI6ICJhIiwgImxhYmVsIjogIuC4reC5iOC4suC4mSByZXBvIiwgImRlc2MiOiAiIiwgImNhdGVnb3J5IjogIuC4quC4geC4tOC4pSJ9LCB7ImlkIjogImIiLCAibGFiZWwiOiAi4LiV4Lij4Lin4LiI4Lil4Li04LiH4LiB4LmMIiwgImRlc2MiOiAiIiwgImNhdGVnb3J5IjogIuC4quC4hOC4o-C4tOC4m-C4leC5jCJ9LCB7ImlkIjogImMiLCAibGFiZWwiOiAi4LiV4Lij4Lin4LiI4LmC4LiE4Lij4LiH4Liq4Lij4LmJ4Liy4LiHIiwgImRlc2MiOiAiIiwgImNhdGVnb3J5IjogIuC4quC4hOC4o-C4tOC4m-C4leC5jCJ9LCB7ImlkIjogImQiLCAibGFiZWwiOiAi4LiU4Li54Lic4LilIiwgImRlc2MiOiAiIiwgImNhdGVnb3J5IjogIuC4hOC4uOC4kyJ9XSwgImVkZ2VzIjogW3sic291cmNlIjogImEiLCAidGFyZ2V0IjogImIifSwgeyJzb3VyY2UiOiAiYiIsICJ0YXJnZXQiOiAiYyJ9LCB7InNvdXJjZSI6ICJjIiwgInRhcmdldCI6ICJkIn1dfQ" width="100%"> | **หลายเข้าหนึ่ง**<br/>หลายแหล่งรวมเป็นผลเดียว<br/><img alt="แผนภาพ หลายเข้าหนึ่ง: หลายแหล่งรวมเป็นผลเดียว" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJmYW5pbiIsICJ0aXRsZSI6ICLguILguYnguK3guKHguLnguKXguJfguLXguYjguKPguKfguKHguYDguJvguYfguJkgUkVBRE1FIiwgIm5vZGVzIjogW3siaWQiOiAiYSIsICJsYWJlbCI6ICJtYW5pZmVzdCIsICJkZXNjIjogIiJ9LCB7ImlkIjogImIiLCAibGFiZWwiOiAiQ0kiLCAiZGVzYyI6ICIifSwgeyJpZCI6ICJjIiwgImxhYmVsIjogIuC5guC4hOC5ieC4lCIsICJkZXNjIjogIiJ9LCB7ImlkIjogImQiLCAibGFiZWwiOiAiUkVBRE1FIiwgImRlc2MiOiAiIn1dfQ" width="100%"> |
| **เป็นชั้น (preset)**<br/>UI, API, DB<br/><img alt="แผนภาพ preset stack: UI, API, DB" src="https://hyperweave.app/v1/diagram/stack/primer.static?variant=porcelain&face=light" width="100%"> | **ลูป (preset)**<br/>วงล้อที่หมุนต่อเนื่อง<br/><img alt="แผนภาพ preset loop-flywheel: วงล้อที่หมุนต่อเนื่อง" src="https://hyperweave.app/v1/diagram/loop-flywheel/primer.static?variant=porcelain&face=light" width="100%"> |

อีก 4 แบบที่ใช้บ่อยคือ `pipeline`, `fanout`, `dag` และ matrix อยู่ในหัวข้อก่อนหน้าและหัวข้อสถาปัตยกรรม ที่เหลืออยู่ในรายการ preset 59 แบบของ `references/hyperweave-catalog.md`

</details>

## เริ่มต้นใช้งาน

### สิ่งที่ต้องมี

- Claude ที่ใช้สกิลได้ (Claude Code, Claude Desktop หรืออื่นที่อ่าน `SKILL.md`)
- Python 3 สำหรับสคริปต์ตรวจใน `scripts/`
- อินเทอร์เน็ต เพราะ `check_images.py` ต้องดึงภาพจาก hyperweave.app มาตรวจ
- HyperWeave MCP (`hw_compose`, `hw_validate`, `hw_discover`) ใช้ลองสเปกภาพได้ แต่ไม่บังคับ ถ้าไม่มีสกิลยังทำ README ได้โดยใช้ลิงก์ภาพตรง

### ติดตั้ง

1. ถ้าได้ไฟล์ `repo-readme-hyperweave.skill` มา เปิดแล้วกด Save skill

2. หรือคัดลอกทั้งโฟลเดอร์ไปไว้ที่ที่ Claude อ่านสกิล (ของ Claude Code คือ `~/.claude/skills/` ซึ่งเป็นตำแหน่งมาตรฐาน ไม่ได้กำหนดใน repo นี้)

   ```bash
   cp -r repo-readme-hyperweave ~/.claude/skills/
   ```

3. เปิด session ใหม่ให้ Claude โหลดสกิล

## วิธีใช้

### ลองใน 30 วินาที

เปิด Claude ในโฟลเดอร์ของ repo ที่อยากทำ README แล้วพิมพ์

```text
อ่าน repo นี้แล้วทำ README ภาษาไทยสวยๆ ด้วย hyperweave
```

สกิลจะทำตามลำดับในหัวข้อ [สถาปัตยกรรม](#สถาปัตยกรรม) แล้วบอกท้ายงานว่าใช้โครงขนาดไหน เลือกสไตล์อะไร เพราะอะไร และมีอะไรใน README เดิมที่ไม่ตรงกับโค้ด

### สคริปต์ตรวจ

สกิลรันสามตัวนี้เองก่อนส่งงาน รันเองก็ได้ ใส่ `PYTHONUTF8=1` บน Windows ไม่งั้นพิมพ์ภาษาไทยแล้ว error

```bash
PYTHONUTF8=1 python scripts/check_images.py README.md
```

```bash
PYTHONUTF8=1 python scripts/lint_structure.py README.md --tier normal
```

```bash
PYTHONUTF8=1 python scripts/lint_readme.py README.md
```

| สคริปต์ | ตรวจอะไร | ล้มเหลวเมื่อ |
|---|---|---|
| `check_images.py` | ภาพ hyperweave.app ทุกลิงก์โหลดได้และไม่ใช่ภาพ error พร้อมบอกเหตุผลที่ภาพ error ระบุ และเตือน (CHECK) ให้ตรวจเองกับไอคอน การ์ด กราฟ และข้อมูลสด | ลิงก์ `/v1/a/`, ภาพ error, เปิดไม่ได้ |
| `lint_structure.py` | H1 ตัวเดียว, ระดับหัวข้อไม่ข้าม, มีติดตั้ง/วิธีใช้/ใบอนุญาต, สารบัญและลิงก์, code block มีภาษา, alt, รูปซ้ำ, ลิงก์ในไฟล์, placeholder | มีรายการ FAIL |
| `lint_readme.py` | emoji และสำนวนโฆษณาหรือสำนวนที่ฟังเหมือน AI | พบสำนวนหรือ emoji |

ตัวเลือก `--tier tiny` ของ `lint_structure.py` ปิดข้อบังคับสารบัญสำหรับ repo เล็ก

## โครงสร้างโปรเจกต์

<details>
<summary>ดูแผนผังไฟล์</summary>

<br/>

```text
SKILL.md                         ขั้นตอนทั้งหมดที่ Claude อ่านเมื่อสกิลทำงาน
references/readme-structure.md   โครงหัวข้อมาตรฐานและกฎตามขนาดกับประเภท repo
references/hyperweave-catalog.md  รายการสิ่งที่ HyperWeave ทำได้ ใช้ตอนเลือกภาพ
scripts/check_images.py          ตรวจลิงก์ภาพ
scripts/lint_structure.py        ตรวจโครงสร้าง
scripts/lint_readme.py           ตรวจสำนวนและ emoji
evals/                           โจทย์ทดสอบ 4 ข้อ (prompt, case.yaml, graders)
```

</details>

ไฟล์ที่ Claude อ่านตอนใช้งานคือ `SKILL.md` กับ `references/` ส่วน `evals/` ไว้ทดสอบสกิลเท่านั้น

## สถาปัตยกรรม

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://hyperweave.app/v1/diagram/custom/primer.static?variant=noir&face=dark&spec=eyJ0b3BvbG9neSI6ICJwaXBlbGluZSIsICJ0aXRsZSI6ICLguILguLHguYnguJnguJXguK3guJnguJfguLXguYjguKrguIHguLTguKXguJfguLMiLCAibm9kZXMiOiBbeyJsYWJlbCI6ICLguK3guYjguLLguJkgcmVwbyIsICJkZXNjIjogIm1hbmlmZXN0LCDguKrguITguKPguLTguJvguJXguYwsIENJIn0sIHsibGFiZWwiOiAi4Lin4Liy4LiH4LmC4LiE4Lij4LiHIiwgImRlc2MiOiAi4Lir4Lix4Lin4LiC4LmJ4Lit4Lih4Liy4LiV4Lij4LiQ4Liy4LiZIn0sIHsibGFiZWwiOiAi4LmA4Lil4Li34Lit4LiB4Liq4LmE4LiV4Lil4LmMIiwgImRlc2MiOiAiNCDguYHguJrguJoifSwgeyJsYWJlbCI6ICLguKrguKPguYnguLLguIfguKDguLLguJ4iLCAiZGVzYyI6ICLguKXguLTguIfguIHguYzguJfguLXguYjguYLguKvguKXguJTguYTguJTguYnguIjguKPguLTguIcifSwgeyJsYWJlbCI6ICLguYDguILguLXguKLguJnguYTguJfguKIiLCAiZGVzYyI6ICLguITguLPguITguLjguYnguJnguYDguITguKIifSwgeyJsYWJlbCI6ICLguJXguKPguKfguIgiLCAiZGVzYyI6ICIzIOC4quC4hOC4o-C4tOC4m-C4leC5jCJ9XX0">
  <img alt="ขั้นตอนของสกิล: อ่าน repo, วางโครง, เลือกสไตล์, สร้างภาพ, เขียนไทย, ตรวจ" src="https://hyperweave.app/v1/diagram/custom/primer.static?variant=porcelain&face=light&spec=eyJ0b3BvbG9neSI6ICJwaXBlbGluZSIsICJ0aXRsZSI6ICLguILguLHguYnguJnguJXguK3guJnguJfguLXguYjguKrguIHguLTguKXguJfguLMiLCAibm9kZXMiOiBbeyJsYWJlbCI6ICLguK3guYjguLLguJkgcmVwbyIsICJkZXNjIjogIm1hbmlmZXN0LCDguKrguITguKPguLTguJvguJXguYwsIENJIn0sIHsibGFiZWwiOiAi4Lin4Liy4LiH4LmC4LiE4Lij4LiHIiwgImRlc2MiOiAi4Lir4Lix4Lin4LiC4LmJ4Lit4Lih4Liy4LiV4Lij4LiQ4Liy4LiZIn0sIHsibGFiZWwiOiAi4LmA4Lil4Li34Lit4LiB4Liq4LmE4LiV4Lil4LmMIiwgImRlc2MiOiAiNCDguYHguJrguJoifSwgeyJsYWJlbCI6ICLguKrguKPguYnguLLguIfguKDguLLguJ4iLCAiZGVzYyI6ICLguKXguLTguIfguIHguYzguJfguLXguYjguYLguKvguKXguJTguYTguJTguYnguIjguKPguLTguIcifSwgeyJsYWJlbCI6ICLguYDguILguLXguKLguJnguYTguJfguKIiLCAiZGVzYyI6ICLguITguLPguITguLjguYnguJnguYDguITguKIifSwgeyJsYWJlbCI6ICLguJXguKPguKfguIgiLCAiZGVzYyI6ICIzIOC4quC4hOC4o-C4tOC4m-C4leC5jCJ9XX0">
</picture>

เรียงตามที่ `SKILL.md` สั่ง ขั้นอ่าน repo ต้องจบก่อนเขียนทุกครั้ง ถ้าโค้ดกับ README เดิมไม่ตรงกัน ให้ยึดโค้ด ขั้นสร้างภาพใช้ลิงก์ที่เข้ารหัสสเปกไว้ในตัว เลยเปิดได้จากทุกเครื่อง และขั้นตรวจจะเปิดทุกลิงก์เพื่อดูว่าไม่ได้เป็นภาพ error

## ทดสอบ

โจทย์ทดสอบอยู่ใน `evals/` มี 4 repo ตัวอย่าง คือ CLI เล็กๆ, API ร้านค้า, แอปโน้ตที่ README เดิมไม่ตรงกับโค้ด และชุดสกิลที่มี 11 ตัว แต่ละโจทย์มีเงื่อนไขตรวจเป็นข้อๆ ใน `graders/` รันด้วยสกิล skill-creator ซึ่งเป็นเครื่องมือแยกจาก repo นี้

ผลรอบล่าสุด สกิลนี้ผ่านเงื่อนไขทั้งหมด ส่วนสกิลเวอร์ชันก่อนหน้าผ่านราว 80% รันรอบเดียวต่อโจทย์ จึงเป็นสัญญาณคร่าวๆ ไม่ใช่ตัวเลขที่เชื่อถือทางสถิติ

## ข้อจำกัดและสิ่งที่ยังไม่ได้ทำ

- ภาพทุกภาพส่งจากเซิร์ฟเวอร์ hyperweave.app ชื่อที่ใส่ใน label จะอยู่ใน URL สาธารณะ สกิลจึงถามก่อนสำหรับ repo ส่วนตัว และถ้าเว็บนั้นล่ม ภาพจะไม่ขึ้น
- ภาพตารางแบบสว่างกับแบบมืดเคยออกมาเหมือนกันทุกไบต์ในการทดสอบครั้งหนึ่ง จึงควรเปิดดูทั้งสองแบบก่อนใช้คู่ `<picture>`
- ไอคอนที่ชื่อไม่มีอยู่ การ์ดของผู้ใช้ที่ไม่มีจริง และข้อมูลสดของแพ็กเกจที่ไม่มี ยังเรนเดอร์ออกมาเหมือนปกติ ตัวตรวจจับไม่ได้ จึงต้องยืนยันชื่อจาก manifest และ git remote แล้วเปิดดูภาพเอง
- `loop` ใช้ preset เท่านั้น เพราะสเปกเขียนเองมีกฎเข้มและยังไม่เคยเขียนผ่านในการทดสอบ
- สไตล์ Premium (chrome) ยังไม่เคยทดสอบกับ repo จริง
- ยังไม่ได้ปรับ description ในหัวไฟล์ `SKILL.md` ให้ถูกเรียกใช้แม่น ตัวทดสอบรอบก่อนวัดไม่ได้ ถ้า Claude ไม่เรียกสกิลเอง ให้พิมพ์ชื่อสกิลตรงๆ
- ความรู้สึกว่า "ไทยเป็นธรรมชาติ ไม่เหมือน AI" ตัวสคริปต์ตรวจได้แค่คำที่รู้จัก ที่เหลือต้องให้คนอ่าน
- ยังไม่มีโหมดสร้าง README ภาษาอังกฤษ

## ร่วมพัฒนา

repo นี้ยังไม่มีไฟล์ `CONTRIBUTING.md` ถ้าจะแก้สกิล

1. แก้ `SKILL.md` หรือ `references/readme-structure.md`
2. รันโจทย์ใน `evals/` ด้วย skill-creator เทียบกับเวอร์ชันก่อนแก้
3. ถ้าแก้สคริปต์ ลองรันกับ README ตัวอย่างที่มีทั้งแบบผ่านและแบบมีปัญหา ดูว่าสคริปต์ยังจับได้

## ใบอนุญาต

MIT ดูรายละเอียดในไฟล์ [LICENSE](LICENSE)
