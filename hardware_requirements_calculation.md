# Hardware Requirements — GeoSpectra Lab v0.1.24 Rerun

**Date:** 2026-05-31  
**Based on:** OOM incident 2026-05-25, measured peak RSS 10.5 GiB на N=128 j_max=3

---

## 📊 Измеренные факты

- **Peak anon-rss:** 10.5 GiB (11 004 124 kB) — scipy.linalg.eigh на N=128 j_max=3
- **Hilbert dim:** 7680 (N=128 × S³_dim=60 для j_max=3)
- **Matrix storage:** 0.94 GiB (input) + 0.94 GiB (eigenvectors)
- **LAPACK workspace:** 2-4× matrix size (per thread, с учётом OPENBLAS_NUM_THREADS=4)
- **OOM ceiling:** 15 GiB RAM (Hetzner CPX42) минус 4.4 GiB другие сервисы = ~10 GiB доступно

---

## 🎯 Требования к RAM с запасом

| Подход | Multiplier | Требуется | Ближайший стандарт |
|---|---|---|---|
| **Консервативный (50% safety)** | 1.5× | 15.8 GiB | **64 GiB** |
| **Осторожный (100% safety)** | 2.0× | 21.0 GiB | **64 GiB** |
| **Параноидальный (150% safety)** | 2.5× | 26.2 GiB | **64 GiB** |

**Вывод:** Минимум **64 GiB RAM** с 50% safety margin.

---

## 💰 Варианты железа

### Вариант A: Hetzner Dedicated (краткосрочная аренда)

| Модель | RAM | CPU | Цена | Margin | Peak RSS % | Годится? |
|---|---|---|---|---|---|---|
| **AX42** | 64 GiB | Ryzen 7 3700X (8c/16t) | €47.50/мес | 510% | 16% | ✅ Минимум |
| **AX52** | 128 GiB | Ryzen 9 5950X (16c/32t) | €69.90/мес | 1119% | 8% | ✅ Комфорт |
| AX102 | 256 GiB | Ryzen 9 7950X3D (16c/32t) | €149.90/мес | 2338% | 4% | Overkill |

**Рекомендация для quick rerun:** **AX42** (64 GiB, €47.50/мес)

**Почему:**
- Peak RSS 10.5 GiB × 1.5 safety = 15.8 GiB → 64 GiB даёт **510% margin**
- Smoke test займёт **16% RAM** (остаётся 53.5 GiB для OS + буферов)
- Стоимость **1-2 дня аренды:** ~€3-6 (при почасовой оплате, если доступно)
- Если нет почасовой — €47.50 за месяц (минимальный billing period у Hetzner)

**Время выполнения full rerun (216 cases):**
- Heavy cases (N=128 j_max=3): ~24 cases × 10 min = **4 часа**
- Medium cases (N=64): ~72 cases × 2 min = **2.5 часа**
- Light cases (N≤32): ~120 cases × 0.5 min = **1 час**
- **ИТОГО:** ~7-10 часов compute + 2-3 часа setup/verify = **12-15 часов wall time**

---

### Вариант B: Собрать локально (долгосрочное владение)

| Компонент | Спецификация | Цена (ориентир) |
|---|---|---|
| **RAM** | DDR4 64GB (4×16 GB 3200 MHz) | ~$80-100 |
| **CPU** | AMD Ryzen 7 5700X (8c/16t) | ~$150 |
| **Материнка** | B550 (AM4, 4 слота RAM) | ~$80 |
| **PSU** | 550W 80+ Bronze | ~$50 |
| **Корпус** | Средний tower + охлаждение | ~$70 |
| **Storage** | NVMe 1TB (для datasets) | ~$60 |
| **ИТОГО** | | **~$490-550** |

**Окупаемость:**
- Hetzner AX42: €47.50/мес × 12 = **€570/год** (~$620)
- Своя сборка: **$490** → окупается за **10 месяцев**
- После окупаемости — unlimited compute time бесплатно

**Дополнительные выгоды:**
- Можно использовать для других проектов (Reflexio, ARCHCODE, VeriFind, etc.)
- Полный контроль (нет ограничений по времени, нет kill после idle)
- Можно апгрейдить (добавить GPU, больше RAM, NVMe расширение)
- Локально — нет latency для rsync artifacts, нет опасений про privacy datasets

**Минусы:**
- Нужно физическое пространство + электричество (~100W idle, ~200W load)
- Setup time ~2-3 часа (сборка + OS install + packages)
- No enterprise-level uptime (но для research compute — не критично)

---

### Вариант C: Hetzner Cloud (CPX / CCX серия) — НЕ РЕКОМЕНДУЕТСЯ

| Модель | RAM | vCPU | Цена | Почему НЕ подходит |
|---|---|---|---|---|
| CPX51 | 16 GB | 16 shared | €57.90/мес | Shared vCPU + no swap = OOM риск |
| CCX33 | 32 GB | 8 dedicated | €81.90/мес | Dedicated, но дороже чем AX42 при меньше RAM |
| CCX63 | 128 GB | 32 dedicated | €327.90/мес | Overkill по CPU, дороже в 5× чем AX42 |

**Вердикт:** Cloud-серия дороже dedicated при тех же specs. Для multi-hour dense eigh — dedicated выгоднее.

---

## ✅ Финальная рекомендация

### Для быстрого одноразового rerun (если не планируешь frequent compute)

**Hetzner AX42: 64 GiB RAM, 8c/16t, €47.50/мес**

**План действий:**
1. Заказать AX42 (setup time ~24 часа у Hetzner)
2. Setup environment (2-3 часа: Python venv, packages, git clone, ssh keys)
3. Smoke test N=128 j_max=3 (30 минут)
4. Full rerun (10-12 часов)
5. rsync artifacts обратно локально
6. Отменить server после завершения (проплатишь 1 месяц минимум = €47.50)

**Риск:** Минимальный billing period 1 месяц → €47.50 даже если используешь 2 дня.

---

### Для долгосрочной работы (если compute будет повторяться)

**Собрать локально: 64 GiB DDR4 + Ryzen 7 5700X, ~$490**

**План действий:**
1. Купить железо (доставка 1-5 дней)
2. Собрать (2-3 часа)
3. Ubuntu Server 22.04 / 24.04 LTS install (1 час)
4. Setup Python stack (1 час)
5. Smoke test (30 мин)
6. Full rerun (10-12 часов)
7. Оставить железо для будущих compute (Negative Controls, Gate 5, W-sweep, Reflexio, etc.)

**Риск:** Upfront cost $490, но окупается за 10 месяцев против аренды.

---

## 🔥 Что делать сейчас

**Если хочешь начать rerun ASAP (в течение недели):**
→ **Hetzner AX42** — заказ сегодня, ready через 24-48 часов

**Если можешь подождать 1-2 недели:**
→ **Собрать локально** — лучше ROI, unlimited future use

**Гибрид (если неуверен):**
1. Заказать AX42 для первого rerun (€47.50)
2. Пока идёт rerun — купить железо локально
3. После первого rerun на AX42 — отменить Hetzner, перейти на локальное
4. Total cost: €47.50 + $490 = ~$540, но получаешь:
   - Immediate start (AX42 ready за 24ч)
   - Long-term ownership (local build)
   - Fallback option (если local build проблемы — уже знаешь что AX42 работает)

---

## 📝 Детали для заказа

### Hetzner AX42

**Specs:**
- AMD Ryzen 7 3700X (8 cores / 16 threads, 3.6 GHz base, 4.4 GHz boost)
- 64 GB DDR4 ECC RAM
- 2× 512 GB NVMe SSD (hardware RAID1 или software RAID)
- 1 Gbit/s uplink, unlimited traffic
- Location: Falkenstein (DE) или Helsinki (FI) — выбирай ближайший к Казахстану
- €47.50/мес, setup fee €0 (иногда Hetzner waives setup fee на dedicated)

**Ссылка:** https://www.hetzner.com/dedicated-rootserver/ax42

**Setup time:** 24 часа (обычно), может быть быстрее если stock available

---

### Local Build (64 GB)

**Пример конфигурации (US prices, adjust for KZ availability):**

- **RAM:** Corsair Vengeance LPX 64GB (4×16GB) DDR4 3200MHz CL16 — ~$90 (AliExpress/Wildberries)
- **CPU:** AMD Ryzen 7 5700X (8c/16t, AM4) — ~$150 (б/у можно найти $120)
- **Motherboard:** MSI B550-A PRO (AM4, ATX, 4 DIMM slots) — ~$80
- **PSU:** EVGA 600 BR 80+ Bronze 600W — ~$50
- **Case:** Fractal Design Focus G (mid-tower, good airflow) — ~$50
- **Cooler:** Stock Wraith cooler (included с 5700X) или Deepcool AK400 ~$30
- **NVMe:** Kingston NV2 1TB PCIe 4.0 — ~$60

**Где купить в KZ:**
- Kaspi.kz (Corsair RAM, AMD CPU часто есть)
- Kompas.kz (компьютерные компоненты Алматы)
- AliExpress (если можешь подождать доставку 1-2 недели)

---

## ⚠️ Важные ограничения

1. **Per-case checkpointing REQUIRED** — без этого любой OOM/kill потеряет прогресс.
2. **Smoke test FIRST** — не запускать full rerun без smoke N=128 j_max=3 прежде.
3. **BLAS threads limit** — `export OPENBLAS_NUM_THREADS=4` (см. Memory-Safe Rerun Plan).
4. **No auto-chain** — smoke pass → ask user → full rerun (не автоматически).

---

**Записано:** 2026-05-31  
**Source:** `reports/INCIDENT_GATE4B_v0.1.24_OOM_2026-05-25.md`, `reports/MEMORY_SAFE_RERUN_PLAN_v0.1.24.md`
