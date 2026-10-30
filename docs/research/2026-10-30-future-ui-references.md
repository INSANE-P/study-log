# 미래형 유리 화면 근거 조사 (2026-10-30)

화면을 "미래지향적, 홀로그램 유리, 화려하지만 가독성 있게, 어디 따라한 느낌 없이"로 다시 디자인하기 전에 모은 근거다. 결정은 하지 않고 재료만 모은다. 대표 장면 후보는 FSRS 의 기억 확률(retrievability)을 홀로그램 신호가 흐려지는 모습으로 보여 주는 것이다.

## 읽는 법

- **확인함**: 2026-10-30 에 원문(공식 문서, 표준 문서, 논문 본문, 회사 공식 블로그, 당사자 인터뷰 원문, 공식 소스)을 직접 열어 본 것
- **확인 전**: 2차 글(블로그, 요약 사이트, 검색 요약)에서만 봤거나 원문이 열리지 않은 것. 쓰기 전에 원문을 다시 찾는다
- **관행**: 연구가 아니라 도구나 사람들이 쓰는 규칙. 숫자를 근거로 쓰지 않는다
- **우리 판단**: 원문에 없는, 이 문서를 쓰면서 내린 해석. 근거 문장과 섞지 않으려고 따로 표시한다
- 모든 출처의 확인 날짜는 2026-10-30 이다
- 이전 조사(`2026-10-30-design-references.md`)에 이미 있는 것은 다시 적지 않는다

## 답이 필요했던 질문

1. 유리 재질을 어느 층에 쓰고 어디에 쓰지 말라고 하나. 글자 대비는 어떻게 지키라고 하나
2. 반투명 위에서 WCAG 대비를 어떻게 재나. 투명도 줄이기 설정을 웹에서 받을 수 있나
3. 영화와 게임 UI 를 만든 사람들은 화려함과 읽힘을 어떻게 같이 가져가나
4. AI 가 만든 미래형 화면의 흔한 꼴 중 이전 조사에 없던 것은
5. 줄어드는 값을 밝기, 흐림, 노이즈로 보여 줄 때 사람이 얼마나 정확히 읽나
6. 웹에서 셰이더 없이 어디까지 되고 비용은 얼마인가

---

## 1. 유리(반투명) UI 공식 지침

### 1-1. Apple Liquid Glass (2025)

- **확인함 (Apple Newsroom, 2025-06-09)**: 반투명 재질이 주변을 비추고 굴절하며, 색은 주변 콘텐츠에서 온다. 컨트롤은 앱 위에 놓인 "별도의 기능 층"이다. 밝은 곳과 어두운 곳에 맞춰 바뀐다. iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26 에 걸친다. 글자 대비나 접근성 이야기는 이 보도자료에 없다
  - 출처: https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/
- **확인함 (HIG Materials, 변경 기록 2025-06-09 추가, 2025-09-09 갱신)**
  - Liquid Glass 는 탭 바, 사이드바 같은 컨트롤과 내비게이션을 위한 층이고, 콘텐츠 층 위에 뜬다
  - **콘텐츠 층에는 쓰지 않는다.** 콘텐츠 층의 앱 바탕 같은 곳에는 표준 머티리얼을 쓴다. 예외는 슬라이더, 토글처럼 누르는 순간에만 유리 모양이 되는 컨트롤
  - **아껴 쓴다.** 직접 만든 컨트롤에 넣을 때는 앱에서 가장 중요한 기능 요소로 한정한다. 여러 곳에 쓰면 콘텐츠에서 주의를 빼앗는다
  - 두 변형: **regular** 는 뒤 콘텐츠를 흐리게 하고 밝기를 조절해 글자를 지킨다. 글이 많은 요소(알림, 사이드바, 팝오버)에 쓴다. **clear** 는 매우 투명해서 사진, 영상 같은 풍부한 바탕 위에만 쓴다
  - clear 아래 콘텐츠가 밝으면 **35% 불투명도의 어두운 디밍 층**을 깔 것을 고려한다. 콘텐츠가 충분히 어두우면 필요 없다
  - 표준 머티리얼 위 글자는 시스템의 vibrant 색을 쓴다. 두꺼운(불투명한) 머티리얼일수록 가는 글자에 대비가 좋고, 얇은 머티리얼은 맥락을 보여 주는 대신 대비가 약하다
  - 사람이 투명도 줄이기, 대비 높이기를 켜면 변형의 모양이 달라진다
  - 출처: https://developer.apple.com/design/human-interface-guidelines/materials (본문은 자바스크립트로 그려져 같은 내용의 공식 JSON https://developer.apple.com/tutorials/data/design/human-interface-guidelines/materials.json 으로 읽었다)
- **확인함 (HIG Color 의 Liquid Glass color 절)**: 유리는 원래 색이 없고 뒤 콘텐츠의 색을 받는다. 색은 상태 표시나 주요 동작처럼 정말 강조가 필요한 곳에만, 그것도 글자보다 바탕에 넣는다. 여러 컨트롤의 바탕에 색을 넣지 않는다. 작은 요소(툴바, 탭 바)의 글자와 기호는 뒤가 밝으면 어둡게, 어두우면 밝게 바뀌고, 큰 요소(사이드바)는 복잡한 바탕에서 읽히도록 더 불투명해진다. 스크롤되는 색 콘텐츠가 잠깐 지나가는 건 괜찮아도, 멈춘 상태(화면 맨 위)에서는 분명히 읽혀야 한다
  - 출처: https://developer.apple.com/design/human-interface-guidelines/color
- **확인함 (WWDC25 세션 219 "Meet Liquid Glass" 페이지의 대본)**
  - 예전 재질이 빛을 흩뜨렸다면 이 재질은 빛을 휘고 모으는 렌즈 효과로 정체성을 만든다. 요소는 그냥 사라지지 않고 굴절을 서서히 바꾸며 나타나고 사라진다
  - 크기와 주변에 맞춰 바뀐다. 큰 유리는 더 두꺼운 재질처럼 그림자와 굴절이 깊어진다
  - 유리는 콘텐츠 위에 뜨는 내비게이션 층에 두고, 표 같은 콘텐츠는 콘텐츠 층에 둔다
  - **유리 위에 유리를 올리지 않는다.** 유리 위 요소는 채움, 투명도, vibrancy 로 재질의 일부처럼 보이게 한다
  - regular 와 clear 를 섞지 않는다. clear 는 (1) 미디어가 많은 바탕 위, (2) 디밍 층을 넣어도 콘텐츠가 망가지지 않을 때, (3) 위의 내용이 굵고 밝을 때, 세 조건이 모두 맞을 때만
  - 모든 요소에 색을 입히지 않는다. 멈춘 상태에서는 콘텐츠와 유리가 겹치지 않게 배치한다
  - 투명도 줄이기를 켜면 더 서리 낀 유리가 되어 뒤를 더 가리고, 대비 높이기를 켜면 거의 검정이나 흰색에 대비 테두리가 붙고, 동작 줄이기를 켜면 효과가 약해지고 탄성이 꺼진다
  - 출처: https://developer.apple.com/videos/play/wwdc2025/219/

### 1-2. visionOS 의 glass 와 깊이

- **확인함 (HIG Materials 의 visionOS 절)**: 창은 바꿀 수 없는 시스템 재질 glass 를 쓴다. 뒤 색 정보의 범위를 제한해 창 안 콘텐츠의 대비를 지키면서, 주변에 따라 밝아지거나 어두워진다. 따로 다크 모드가 없다. 창에서는 불투명한 색보다 반투명을 택하라고 한다(불투명은 주변 인식을 막는다). 그 위 글자는 vibrancy 세 단계(label, secondaryLabel, tertiaryLabel)로 위계를 만들고, 가장 약한 단계는 비활성처럼 읽힘이 덜 중요할 때만
  - 출처: https://developer.apple.com/design/human-interface-guidelines/materials
- **확인함 (HIG Spatial layout 의 Depth 절, 변경 기록 2024-03-29)**
  - 깊이로 위계를 전한다. 시트가 뜨면 뒤 창이 z축으로 물러나고 시트가 앞으로 나온다
  - **글자에는 깊이를 넣지 않는다.** 바탕 위에 떠 보이는 글자는 읽기 어렵고 눈이 불편할 수 있다
  - 깊이는 큰 중요 요소(탭 바, 툴바를 창에서 띄우기)에 좋고, 작은 것(버튼 기호를 바탕에서 띄우기)에는 오히려 덜 읽힌다. 깊이 차이마다 눈 초점을 다시 맞춰야 하므로 너무 자주 바꾸면 피곤하다
  - 몰입 화면에서는 주변부에 산만한 움직임이나 밝고 대비 큰 물체를 두지 않는다
  - 출처: https://developer.apple.com/design/human-interface-guidelines/spatial-layout
- **확인함 (HIG Color 의 visionOS 절)**: 눈이 어둠에 적응했을 때 높은 대비는 불편할 수 있다. 매우 어두운 바탕 위의 밝은 물체, 특히 깜빡이거나 움직이는 것을 피한다
  - 출처: https://developer.apple.com/design/human-interface-guidelines/color

### 1-3. Microsoft Fluent Acrylic 과 Mica

- **확인함 (Acrylic material, Microsoft Learn, 2026-10-02 갱신)**
  - 쓰는 곳: 컨텍스트 메뉴, 플라이아웃, 비모달 팝업 같은 **잠깐 뜨는 면**에는 background acrylic. 스크롤하다 콘텐츠와 겹칠 수 있는 보조 UI 에는 in-app acrylic
  - **콘텐츠를 나누는 세로 패널에는 아크릴 대신 불투명 바탕을 권한다.** 패널이 콘텐츠 위로 열릴 때만 아크릴
  - 하지 말 것: 앱의 큰 바탕면에 desktop acrylic, 아크릴 면 여러 개를 나란히 붙이기(이음매가 보임), 아크릴 여러 겹(착시), **아크릴 위에 강조색 글자**(기본 14px 에서 최소 대비를 못 넘기 쉽다), 아크릴 위 하이퍼링크
  - 구성: 바탕 → 흐림 → exclusion 혼합 층(대비와 읽힘을 위해) → 색조 → 노이즈
  - 렌더링이 GPU 를 많이 써 전력과 배터리를 쓴다. 절전 모드, 저사양 기기, 설정 > 개인 설정 > 색 > 투명 효과 끄기, 고대비 모드에서는 단색으로 바뀐다
  - 출처: https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic
- **확인함 (Mica material, Microsoft Learn, 2026-07-22)**
  - Mica 는 **불투명**하다. 오래 떠 있는 창의 맨 아래 바탕에 쓰고, 바탕 화면 배경을 **한 번만** 샘플링해서 성능을 지킨다. 비활성 창에서는 중립색으로 돌아가 어느 창에 초점이 있는지 알려 준다
  - 층 구조: Mica(바탕) 위에 낮은 불투명도 단색의 콘텐츠 층. Mica Alt 는 바탕 → 명령 층 → 콘텐츠 층 세 겹
  - 배경 재질은 앱에 한 번만 적용한다
  - 출처: https://learn.microsoft.com/en-us/windows/apps/design/style/mica

### 1-4. 세 회사가 겹치는 지점 (우리 판단)

- 셋 다 유리(반투명)를 **콘텐츠가 아닌 위층**(내비게이션, 잠깐 뜨는 면)에 두고, 콘텐츠와 큰 바탕은 불투명하거나 반투명도가 낮은 재질로 둔다
- 셋 다 유리를 겹치지 말라고 한다(Apple: 유리 위 유리 금지, Microsoft: 아크릴 겹치기와 나란히 붙이기 금지)
- 셋 다 유리 위 글자색을 따로 정한다(Apple vibrant 색, Microsoft 강조색 글자 금지)
- 셋 다 사용자 설정(투명도 줄이기, 대비 높이기, 절전)에서 단색으로 바뀌는 길을 시스템이 책임진다. 웹에서는 이것을 우리가 직접 만들어야 한다(2-3)

---

## 2. 유리와 접근성

### 2-1. NN/g

- **확인함 (Megan Brown, NN/g, 2024-06-07, "Glassmorphism: Definition and Best Practices")**
  - 반투명은 불투명도와 배경 흐림 두 가지로 만든다. 30% 흰 사각형에 25px 흐림이면 뒤 모양의 윤곽이 남고, 100px 이면 섞여 버린다
  - 잘 맞는 곳: 그라데이션이나 복잡한 그림 위, 오버레이와 컨텍스트 메뉴, 혼합현실
  - 실패하는 곳: 너무 밝거나 어두운 글자, 영상·사진·애니메이션 같은 바쁜 바탕, 남용. "아껴서" 쓰라고 한다
  - 복잡한 바탕일수록 흐림을 더 세게. 컴포넌트가 놓일 수 있는 **모든 바탕에서** 대비를 확인한다. 바탕을 우리가 정할 수 있으면 단순하거나 단색인 바탕을 쓴다
  - 숫자 기준(흐림 몇 px, 불투명도 몇 %)은 주지 않는다. 바탕 색을 뽑아 대비를 재라고 한다
  - 출처: https://www.nngroup.com/articles/glassmorphism/
- **확인함 (Raluca Budiu, NN/g, 2025-10-10, "Liquid Glass Is Cracked, and Usability Suffers in iOS 26")**: 반투명 컨트롤이 콘텐츠 위에서 잘 안 보이고, 글자 위에 글자가 겹치는 경우가 가장 나쁘다고 비판한다. 떠 있는 제목, 검색창, 탭 바가 콘텐츠를 가리고 주의를 다툰다. 움직임을 "움직임을 위한 움직임"이라 부른다. 한 전문가의 비평이고 Apple 의 설명은 담지 않았다
  - 출처: https://www.nngroup.com/articles/liquid-glass/
- **확인 전**: Apple 이 iOS 26 베타 중 투명도를 줄였다는 보도(TechCrunch, mezha.ua). 검색 요약에서만 봤다

### 2-2. WCAG 대비를 반투명 위에서

- **확인함 (WCAG 2.2 Understanding 1.4.3)**: 일반 글자 4.5:1, 큰 글자(18pt 또는 14pt 굵게, 대략 24px 또는 18.5px 굵게) 3:1. 기준값은 반올림하지 않는다(4.499:1 은 실패). 글자색만 정하고 바탕색을 안 정하면 실패. 가늘거나 특이한 글꼴은 안티앨리어싱 때문에 실제보다 흐리게 보이니 굵은 글꼴을 쓰거나 기준을 넉넉히 넘기라고 한다. 투명도나 그라데이션 위 측정법은 이 문서에 직접 없다
  - 출처: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- **확인함 (WCAG 실패 기법 F83, 바탕 그림 위 글자)**: 빠른 확인은 어두운 글자면 그림의 **가장 어두운 곳**, 밝은 글자면 **가장 밝은 곳**과 비교한다. 거기서 기준을 넘으면 통과. 못 넘으면 글자 한 자씩 바로 뒤 바탕과 비교한다
  - 출처: https://www.w3.org/WAI/WCAG22/Techniques/failures/F83
  - **우리 판단**: 유리 패널 위 글자도 같은 방식으로 잰다. 유리 뒤로 지나갈 수 있는 바탕 중 최악의 색(밝은 글자면 가장 밝은 바탕)을 유리의 흐림과 색조를 거친 뒤 색으로 뽑아서 잰다
- **확인함 (WCAG 1.4.11 비텍스트 대비)**: 내용을 이해하는 데 필요한 그래픽 부분은 이웃 색과 3:1. 단, 같은 정보를 글자 라벨이나 값으로 함께 보여 주면 그래픽은 예외가 된다
  - 출처: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- **확인함 (WCAG 2.2.2 일시정지, 정지, 숨기기, A 등급)**: 저절로 시작하고, 5초보다 오래 가고, 다른 콘텐츠와 함께 보이는 움직임, 깜빡임, 스크롤에는 멈추거나 숨기는 수단이 있어야 한다. 꼭 필요한 활동의 일부일 때만 예외
  - 출처: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- **확인함 (WCAG 2.3.1 세 번 번쩍임, A 등급)**: 1초에 세 번 넘게 번쩍이면 안 된다(기준 아래면 예외). 번쩍임은 최대 상대 휘도의 10% 이상 오르내림. 붉은 번쩍임은 따로 정의
  - 출처: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

### 2-3. prefers-reduced-transparency

- **확인함 (MDN, 2026-04-20 수정)**: 투명하거나 반투명한 층 효과를 줄이는 기기 설정을 켰는지 알려 준다. 값은 `no-preference`, `reduce`. **실험 기능이고 Baseline 이 아니다.** Windows 10/11 은 설정 > 개인 설정 > 색 > 투명 효과, macOS 는 접근성 > 디스플레이 > 투명도 줄이기, iOS 는 접근성 > 디스플레이 및 텍스트 크기 > 투명도 줄이기
  - 출처: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-transparency
- **확인함 (MDN browser-compat-data 원본 JSON, main 브랜치)**: Chrome 118 부터, Edge 와 Android Chrome 은 Chrome 과 같음. Firefox 는 113 부터 있지만 `layout.css.prefers-reduced-transparency.enabled` 설정을 켜야 함. **Safari 와 iOS Safari 는 지원 안 함**(webkit.org/b/175497)
  - 출처: https://github.com/mdn/browser-compat-data/blob/main/css/at-rules/media.json
  - 함께 본 것: `prefers-contrast` 는 Chrome 96, Firefox 101, Safari 14.1 부터 지원
- **우리 판단**: 크롬 사이드 패널과 웹은 받을 수 있다. 이 PC(Windows 11)에서 투명 효과를 끄면 바로 시험할 수 있다. 폰 복습 카드를 iPhone Safari 로 열면 받을 수 없으므로, 앱 안에 "투명도 줄이기" 선택을 따로 두거나 폰에서는 처음부터 불투명으로 가는 길을 정해야 한다

### 2-4. backdrop-filter 성능

- **확인함 (web.dev, Adam Argyle, Joe Medley, 2019-07-26)**: "backdrop-filter 는 성능을 해칠 수 있으니 배포 전에 시험하라"는 경고가 있다. 지원하지 않을 때는 폴리필 대신 **미리 흐린 그림**으로 대신하라고 한다(`@supports not (backdrop-filter: none)`). `none` 이 아니면 새 쌓임 맥락을 만든다
  - 출처: https://web.dev/articles/backdrop-filter
- **확인함 (web.dev, "How to create high-performance CSS animations", 2020-10-06)**: 흐림이 들어간 것은 빨간 상자를 그리는 것보다 그리기(paint)가 오래 걸린다. 애니메이션은 transform 과 opacity 로 한정해 합성 단계에서 끝내라. will-change 는 문제가 보일 때만, 바뀌기 직전에 붙이고 끝나면 뗀다
  - 출처: https://web.dev/articles/animations-guide
- **확인함 (MDN backdrop-filter, 2026-04-20 수정)**: Baseline 2024(2024-09 부터 최신 브라우저 공통). 요소나 그 바탕이 반투명이어야 보인다. 효과는 가장 가까운 backdrop root 까지만 닿는다. 부모에 `opacity` 1 미만, `filter`, `mask`, `clip-path`, `mix-blend-mode`, 다른 `backdrop-filter` 가 있으면 그 부모가 root 가 되어 효과가 안 보이는 흔한 함정이 생긴다. MDN 본문에 성능 절은 없다
  - 출처: https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter
  - 지원 버전(browser-compat-data): Chrome 76, Edge 79, Firefox 103(123 전에는 GPU 제조사를 모르는 시스템에서 안 됨), Safari 18(9 부터 `-webkit-` 접두사)
- **확인 못 함**: 흐림 반경이나 면적에 따른 비용 숫자. 공식 문서는 "시험하라"까지만 말한다. 2차 글끼리 "반경이 클수록 비싸다"와 "축소 피라미드라 반경과 거의 무관하다"가 엇갈린다

---

## 3. 화려하지만 읽히는 미래형 화면 사례

각 사례 아래 "티 나는 부분"과 "원리"는 **우리 판단**이다. 근거 문장은 "확인함" 줄에만 있다.

### 3-1. Territory Studio (The Martian, Guardians of the Galaxy, Prometheus)

- **확인함 (Pushing Pixels, David Sheldon-Hicks 인터뷰, 2014-08-07)**: 화면 그래픽은 결국 이야기를 위한 것이고 이야기를 빼앗으면 안 된다. 군사, 의료, 기술 회사의 실제 화면이 어떻게 만들어지고 카메라에 어떻게 찍히는지 조사해서 믿을 만하게 만든다. 작품마다 고유한 시각 언어를 만든다(감독들이 인터페이스를 영화의 브랜드 요소로 본다). Prometheus 는 산호, 말미잘 같은 바닷속 생물에서 색과 형태를 가져왔고, Guardians 는 긁힌 유리와 뿌연 흐림으로 오래 쓴 느낌을 냈다. "낡아 보이는 건 괜찮지만 지루해 보이는 건 싫다"는 취지의 말을 한다
  - 출처: https://www.pushing-pixels.org/2014/08/07/the-craft-of-screen-graphics-and-movie-user-interfaces-interview-with-david-sheldon-hicks-of-territory-studio.html
- **확인함 (Pushing Pixels, Marti Romances, David Sheldon-Hicks, 2016-01-12, The Martian)**: NASA 자문을 받아 거의 모든 데이터를 실제처럼 했다. 관객이 한눈에 상황을 알도록 실제 NASA 화면에 없는 명료함을 더했다. 시대가 섞인 NASA 위젯들을 배치, 색, 글자 크기가 일관된 한 시각 언어로 걸렀다. 문제는 화면 수가 아니라 어수선함이고, 상황에 맞춰 정보의 우선순위를 정한다. 장갑 낀 배우를 위해 큰 컨트롤을 썼다
  - 출처: https://www.pushing-pixels.org/?p=11034
- **티 나는 부분**: 청록 선 그림, 원형 HUD, 의미 없이 흐르는 숫자와 격자, 겹겹이 뜬 반투명 패널
- **원리**: 화면 하나마다 "지금 무슨 일인지" 한 번에 읽히게. 실제 사물(우리에겐 공부 도구와 기록)을 조사해 그 결에서 고유한 언어를 만든다. 배치, 색, 글자 크기를 한 체계로 묶는다

### 3-2. Mark Coleran (Bourne 시리즈 등 영화 화면 디자이너)

- **확인함 (Pushing Pixels 인터뷰, 2021-12-21)**: "실용적 미래주의"라는 자기 방식. 관객이 아는 것에서 출발해 미래를 믿게 하는 고리 하나를 더한다. 모든 화면에는 곧바로 이해되는 "read"가 있어야 한다. 빛, 형태, 움직임, 소리로 시선을 가야 할 곳으로 이끈다. 맥락도 사용자도 이유도 없는 HUD 를 비판하고, 다른 영화를 흉내 내면 참고가 돌고 돌아 뻔해진다고 한다. 영화의 겉모습은 실제 제품으로 그대로 옮겨지지 않고, 실제 소프트웨어는 더 단순하고 일 중심이어야 한다. 목표는 "지금보다 조금 나은 진짜 기계" 같은 화면
  - 출처: https://www.pushing-pixels.org/?p=18414
- **티 나는 부분**: 영화 화면의 세밀한 장식을 실제 도구에 그대로 옮기기
- **원리**: 익숙한 도구(코드 에디터, 플래시카드)에서 출발해 미래 고리는 하나만. 화면마다 한 문장으로 말할 수 있는 read

### 3-3. Perception (Iron Man 2, Black Panther)

- **확인함 (Sci-fi Interfaces 의 Perception 질의응답, Christopher Noessel, 2021-04-13)**: John LePore 는 좋은 가상 인터페이스를 "어떻게 작동하는지 짐작할 만큼의 정보"가 있어서 한눈에 그 기술의 의미가 이해되는 것으로 본다. 개념마다 실현 가능한 경로를 따지고, 기술이 마법처럼 보이는 것을 크게 경계했다. 영화가 설명해 주지 않으니 보이는 것만으로 전해야 한다. 영화 작업과 실제 기술 작업을 "비슷한 두 탐색 경로"로 본다
  - 출처: https://scifiinterfaces.com/category/black-panther-2018/ (같은 글이 여러 분류 페이지에 걸려 있다)
- **확인 전**: "화면에 파란 선만 그리는 것 이상을 하려 한다"는 LePore 의 말(Engadget, 2015 기사 검색 요약), "와칸다 기술은 빛이 아니라 물질이어야 한다"(Fast Company 검색 요약), "트렌드 물결을 경계하라, 관객은 기술에 밝다"(School of Motion 검색 요약). 셋 다 원문을 열지 않았다
- **티 나는 부분**: 빛으로만 된 떠 있는 홀로그램 패널
- **원리**: 신호가 흐려지는 모습에 "왜 그렇게 보이는지" 짐작할 단서가 있어야 한다(예: 마지막 복습 뒤 지난 날짜). 마법처럼 보이면 안 된다

### 3-4. GMUNK (Tron: Legacy, Oblivion)

- **확인 전**: Tron: Legacy 의 홀로그램 그래픽을 맡았고, 인터페이스가 관객을 압도하려는 것이 아니었다는 취지의 말(Pushing Pixels 검색 요약). Inventing Interactive 인터뷰는 인증서 만료로 열리지 않았다
- 공식 사이트나 인터뷰 원문에서 원칙을 확인하지 못했다

### 3-5. Apple visionOS 와 Liquid Glass (1절 참고)

- **티 나는 부분**: 알약 모양 떠 있는 탭 바, 굴절하는 렌즈 테두리, 흰 가장자리 하이라이트
- **원리**: 유리는 기능 층에만, 콘텐츠는 불투명. 깊이는 큰 요소의 위계에만, 글자에는 깊이 없음. 유리 위 유리 없음. 색은 주요 동작 하나에만

### 3-6. Linear

- **확인함 (Linear 공식 블로그 "How we redesigned the Linear UI (part Ⅱ)", Karri Saarinen 외 3명, 2024-03-28)**: 테마 생성을 HSL 에서 LCH 로 바꿨고, 테마마다 변수 98개를 정하던 것을 **바탕색, 강조색, 대비 세 가지**로 줄였다. LCH 로 바탕, 패널, 대화상자, 모달의 높이(elevation)를 다룬다. 높이와 위계는 주로 검정과 흰색의 불투명도로 탐색했다. 대비 변수로 접근성용 아주 높은 대비 테마를 자동으로 만든다. 사이드바, 탭, 머리글, 패널의 시각 소음을 줄였고, 계산에 들어가는 파랑의 양을 제한해 중립적인 느낌으로 갔다. 유리나 흐림 이야기는 없고, LCH 체계가 "높이 있고 반투명한 부분"에 먼저 쓰였다는 언급뿐이다
  - 출처: https://linear.app/now/how-we-redesigned-the-linear-ui (같은 글이 linear.app/blog 주소에도 있다)
- **티 나는 부분 (우리 판단, 원문 근거 없음)**: Linear 의 마케팅 페이지를 닮은 어두운 바탕과 은은한 빛 그라데이션. 이 꼴은 이미 많이 복제되어 "Linear 풍"으로 불린다는 2차 글이 있다(확인 전)
- **원리**: 색을 몇 개의 입력값에서 계산하고, 대비를 변수로 두어 고대비 테마를 공짜로 얻는다. 우리에겐 "유리 불투명도"도 대비 변수에 묶을 수 있다

### 3-7. 확인 못 한 사례

- **Raycast**: 창 디자인이나 유리 재질을 설명한 공식 글을 찾지 못했다
- **Arc**: 검색하지 못했다
- **Nothing OS 의 점 글자(Ndot)**: 공식 페이지(nothing.tech 의 커뮤니티 글로 연결)가 열리지 않았다. 점 행렬 글꼴이 로고를 이루고, Nothing X 앱과 런처에 쓰였다는 내용, 이름이 Ndot 57 이라는 내용, 이후 OS 업데이트에서 줄었다는 사용자 불만은 모두 2차 자료(Fonts In Use, 커뮤니티 글)에서만 봤다(확인 전)
  - **우리 판단**: 점 글자는 지금 "미래형"을 흉내 낼 때 가장 쉽게 티 나는 장치 중 하나다. 쓴다면 Nothing 처럼 브랜드 전체가 아니라, 신호 세기 같은 한 가지 뜻에만

---

## 4. AI 가 만든 미래형 화면의 흔한 꼴 (새로 찾은 것만)

이전 조사 6절에 이미 있는 것: 보라 그라데이션, 어두운 바탕의 밝은 청록, 글자 그라데이션, 장식용 격자 바탕, 어디나 유리와 빛, 빛나는 강조색의 어두운 모드, 작은 라벨의 고정폭 글꼴.

- **확인함 (impeccable, "The visible tells of AI design", 날짜 없음, 다시 열어 미래형 관련만 골랐다)**
  - "Glassmorphism everywhere": 흐림, 유리 카드, 빛나는 테두리를 실제 **층 문제를 풀기 위해서가 아니라 장식으로** 쓴 것
  - "Lazy cool" 예시: 유리 패널, 네온 가장자리, 빛나는 구슬이 쌓이기만 하고 쓰는 데 도움이 안 됨
  - 바탕의 방사형 그라데이션 후광, 구역 뒤의 은은한 스포트라이트: 무엇이 중요한지 설명하지 않고 강조만 한다. 간격, 대비, 분명한 제목으로 시선을 이끌라고 한다
  - "Neon on dark": 기본값으로 나온 사이버펑크
  - 장식용 격자 바탕의 처방: 격자는 캔버스, 지도, 치수를 재야 하는 일에만
  - 출처: https://www.impeccable.style/slop
- **관행 (pixelslop 0.3.8 의 "AI Slop Pattern Catalog", 작성자 표시 없음, npm 패키지 안 문서)**: 자동 탐지 규칙이라 숫자가 있다. 연구 근거는 아니다
  - 유리: backdrop-filter 가 `none` 이 아닌 요소가 "1~2개는 괜찮고 3개 이상이면 패턴". 소스에서 `backdrop-filter: blur` 가 5번 이상이면 패턴
  - 빛나는 강조의 어두운 모드: 바탕 채널 45 이하, 채도 높은 그림자(최대 채널 100 초과, 퍼짐 60 초과)가 2개 넘으면
  - 네온: 어두운 바탕에 최대 채널 200 초과, 채도 0.6 초과 강조 글자가 3개 넘으면
  - 청록: 어두운 바탕에 R 50 미만, G 180 초과, B 200 초과 글자가 2개 넘으면. "해커 터미널과 SaaS 대시보드의 만남"이라 부른다
  - 코드가 아닌 글자에 고정폭 글꼴이 2번 넘게 나오면 "기술 느낌용 고정폭"
  - 출처: https://cdn.jsdelivr.net/npm/pixelslop@0.3.8/dist/skill/resources/ai-slop-patterns.md
- **확인 전**: 보라-파랑 그라데이션이 "2025 년 Tailwind UI 기본값"에서 왔다는 주장, 유리 효과가 2021~2023 학습 데이터에 많았다는 주장(검색 요약 속 블로그들). 인과는 글쓴이의 해석이다
- **우리 판단**: 우리가 원하는 "홀로그램 유리"는 위 목록의 거의 모든 항목과 겉모습이 겹친다. 그래서 "티가 안 나게"의 판정 기준은 겉모습이 아니라 **각 효과가 무슨 뜻을 전하는지 한 문장으로 말할 수 있는가**로 잡는 게 맞다. 빛은 기억 확률 하나에만, 유리는 위층 하나에만

---

## 5. 데이터를 빛과 신호로 보여 주기

### 5-1. 흐림(fuzziness)은 "덜 확실함"으로 직관적으로 읽힌다

- **확인함 (MacEachren 외, "Visual Semiotics & Uncertainty Visualization: An Empirical Study", IEEE TVCG 18(12), 2012, 본문 PDF)**
  - 불확실성을 나타내는 시각 변수 11개의 직관성을 실험했다
  - **흐림(fuzziness), 위치, 명도(value)가 "좋음"**(평균 5.0 초과, 흐림과 위치는 최빈값 7, 최고점)
  - 배열, 크기, **투명도는 "쓸 만함"**
  - **채도, 색상, 방향, 모양은 "쓰지 말 것"**(평균, 중앙값, 최빈값 모두 4.0 미만). 채도는 흔히 불확실성에 직관적이라고 인용되는데도 낮게 나왔다는 점을 저자들이 따로 짚는다
  - **방향이 중요하다**: 한쪽 방향만 직관적이었다. 더 흐릴수록, 더 밝을수록(명도가 연할수록), 더 가려질수록(투명도) 덜 확실하다
  - 지도 위 점 기호로 한 실험이고, 작은 화면에서의 크기 축소와 바탕의 영향은 저자들이 남은 질문으로 꼽는다
  - 출처: https://geography.wisc.edu/cartography/projects/publications/MacEachrenEtAl_2012_TVCG.pdf
- **우리 판단**: "잊혀 갈수록 흐려지는 신호"는 연구가 가장 직관적이라고 본 방향과 맞는다. 채도를 빼는 방식(색이 바래는 것)으로 기억 확률을 보여 주는 건 피한다

### 5-2. 흐림은 눈에 바로 띄지만, 크기를 읽는 축으로는 못 쓴다

- **확인함 (Kosara, Miksch, Hauser, "Focus+Context Taken Literally", IEEE Computer Graphics and Applications, 2002-01/02, 본문 PDF)**
  - 흐림 대비 선명함(Semantic Depth of Field)은 **preattentive** 다. 200ms 만 보여 줘도 방해물 63개 사이에서 선명한 대상을 찾고 위치를 댔다(흐림 정도와 방해물 수에 따라 정확도 90% 넘음). 선명한 대상의 개수 추정도 우연보다 유의하게 나았다
  - 찾는 시간은 흐림과 색 사이에 유의한 차이가 없었고, "빨갛고 선명한 것"처럼 둘을 합쳐도 느려지지 않았다
  - **그러나 흐림을 완전한 시각화 차원으로는 쓸 수 없다.** 흐린 대상끼리 흐림 정도를 비교하는 건 피곤했고 의미 있게 구별하지 못했다. 구별할 수 있는 건 **서너 단계** 정도(추가 실험 필요라고 적음)
  - 흐림은 색과 독립이라 흑백이나 색약 사용자에게도 쓸 수 있다. 흐림으로 작은 디테일(아이콘 등)이 안 읽히게 되지만 맥락 대상에만 적용하니 문제가 아니라고 한다
  - 보는 조건이 다르니 사용자가 "구별되는 최소 흐림"과 "최대 흐림"을 맞추게 하라고 제안한다
  - 출처: https://www.cvast.tuwien.ac.at/sites/default/files/bibcite/165/kos_cgaj2002.pdf
- **우리 판단**: 기억 확률을 연속값 그대로 흐림에 걸면 사람은 그 차이를 못 읽는다. 흐림은 3~4단계(예: 선명 / 조금 흐림 / 많이 흐림)로만 쓰고, 정확한 값은 글자로 따로 둔다. 1.4.11 예외 조건(같은 정보를 글자로)과도 맞는다

### 5-3. 크기를 읽는 정확도 순위

- **확인 전 (Cleveland, McGill, "Graphical Perception", JASA 79(387), 1984)**: 공통 축 위 위치 > 정렬 안 된 축 위 위치 > 길이, 방향, 각도 > 넓이 > 부피, 곡률 > **음영, 채도**(가장 부정확) 순서라는 것. 강의 요약(코넬 INFO 3312)과 검색 요약에서만 봤다. 원문 PDF(북경대 강의 사본)는 접속이 거부되었다. 저자들 스스로 이 순서를 정확한 처방이 아니라 틀이라고 했다는 인용도 2차 자료다
- **확인 전**: Heer, Bostock 2010 의 크라우드소싱 재현(순서가 대체로 유지됨). 논문 페이지가 404 였다
- **확인 못 함**: Healey 의 preattentive 정리 페이지(NCSU). 인증서 오류로 열리지 않았다
- **우리 판단 (확인 전 자료에 기댄 것)**: 밝기와 채도는 "얼마나"를 읽는 데 가장 약한 축으로 알려져 있다. 기억 확률의 크기를 정확히 전해야 하는 곳(기록 화면)에서는 막대 길이나 위치를 쓰고, 빛과 흐림은 "지금 챙길 카드인가"라는 분류 신호로만 쓰는 게 안전하다

### 5-4. 밝기를 단계로 나눌 때

- **확인함 (MDN oklch(), 2026-08-27 수정)**: `oklch()` 의 L 은 "눈으로 느끼는 밝기"이고, `hsl()` 의 L 과 다르다. Baseline 널리 쓰임(2023-05 부터)
  - 출처: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch
- **우리 판단**: 밝기 단계를 만들 때 HSL 이 아니라 OKLCH 의 L 을 같은 간격으로 나눠야 단계가 고르게 보인다. Linear 가 LCH 로 옮긴 이유(3-6)와 같은 방향이다

### 5-5. 망각 곡선과 FSRS 기억 확률

- **확인함 (open-spaced-repetition 공식 위키 "The Algorithm", 2026-07-28 수정)**: R 은 "기억해 낼 확률", S 는 "R 이 90% 가 되는 간격". FSRS-6 의 망각 곡선은 R(t,S) = (1 + factor · t/S)^(−w20), factor 는 R(S,S) = 90% 가 되도록 w20 에서 정한다. 지수 함수가 아니라 거듭제곱 함수라 처음에 빨리 떨어지고 뒤로 갈수록 천천히 떨어진다. 위키에는 v0 부터 FSRS-6 까지 실려 있다
  - 출처: https://github.com/open-spaced-repetition/awesome-fsrs/wiki/The-Algorithm (예전 주소 fsrs4anki 위키는 이 주소로 옮겼다고 적혀 있다)
- **확인함 (ts-fsrs README, npm 최신 6.0.0, 2026-10-28 배포)**: `scheduler.model.forgettingCurve(memoryState, elapsedDays)` 가 0~1 사이 기억 확률을 낸다. `DefaultScheduler()` 는 버전을 안 정하면 **FSRS-7** 을 쓰고, 예시의 목표 기억률(desiredRetention)은 0.9. FSRS-7 은 stability, stabilityFast, difficulty 가 다 필요하고 경과 일수를 소수로 다룬다
  - 출처: https://cdn.jsdelivr.net/npm/ts-fsrs/README.md , https://registry.npmjs.org/ts-fsrs
- **우리 판단**: 목표 기억률이 0.9 면 복습 날 카드의 R 은 대개 0.9 근처다. R 을 0~1 전체에 걸쳐 흐림에 펴면 오늘 보는 카드는 거의 다 선명하게 나온다. 단계 경계는 목표 기억률을 기준으로(예: 목표보다 위 / 목표 근처 / 한참 아래) 잡는 게 맞다. 경계 값은 실제 카드 분포를 보고 정한다

---

## 6. 웹에서 구현할 수단

- **확인함 (MDN backdrop-filter)**: `blur()`, `brightness()`, `contrast()`, `saturate()` 같은 함수와 `url()` 로 SVG 필터를 함께 쓸 수 있다고 문법에 적혀 있다. 예: `url("filters.svg#filter") blur(4px) saturate(150%)`
  - 출처: https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter
- **확인 못 함**: backdrop-filter 의 `url()`(SVG 필터)을 브라우저마다 실제로 지원하는지. browser-compat-data 에 하위 항목이 없다. 유리 굴절을 SVG 로 흉내 내는 2차 글들은 Chromium 에서만 된다고 하지만 확인 전이다
- **확인함 (MDN feTurbulence, 2025-10-27 수정)**: Perlin 난류 함수로 구름, 대리석 같은 질감을 만든다. 속성은 baseFrequency, numOctaves, seed, stitchTiles, type. Baseline 널리 쓰임(2015-07 부터). MDN 에 성능 메모는 없다
  - 출처: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feTurbulence
- **확인함 (MDN feDisplacementMap, 2025-10-27 수정)**: `in2` 그림의 채널 값으로 `in` 그림의 픽셀을 옮긴다. 식은 P'(x,y) ← P(x + scale·(XC(x,y) − 0.5), y + scale·(YC(x,y) − 0.5)). MDN 예시가 바로 feTurbulence 를 in2 로 넣어 원을 일그러뜨리는 것이다. Baseline 널리 쓰임(2015-07 부터)
  - 출처: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap
- **확인함 (W3C Filter Effects Module Level 1)**: 표준 상태는 2018-12-18 Working Draft 다. 목차에 "feDisplacementMap Restrictions" 절이 있지만 본문을 끝까지 읽지 못해 내용은 확인 못 했다
  - 출처: https://www.w3.org/TR/filter-effects-1/
- **확인함 (filter 함수 지원, browser-compat-data)**: CSS `filter` 의 blur, brightness, contrast 등은 Chrome 18, Firefox 35, Safari 6 부터
- **우리 판단 (WebGL 없이 되는 범위)**
  - 유리 면: 반투명 바탕 + `backdrop-filter: blur() saturate()` + 가는 밝은 테두리. 지원 안 할 때와 투명도 줄이기에서는 불투명 바탕
  - 흐려지는 신호: 신호 그림(SVG)에 `filter: blur()` 를 단계별로. 연속 애니메이션이 아니라 단계값을 주면 다시 그리기가 줄어든다
  - 노이즈와 지지직거림: feTurbulence 를 한 번 그려 **정지된 질감**으로 깔고, 움직임은 그 레이어의 transform 이나 opacity 로만 준다. baseFrequency 나 seed 를 매 프레임 바꾸는 애니메이션은 매번 필터를 다시 계산하므로 비쌀 것으로 보인다(공식 숫자 없음, 시험 필요)
  - 홀로그램 일렁임: feDisplacementMap 은 작은 신호 그림에만. 글자에는 걸지 않는다(1-2 visionOS 글자 깊이 금지, 2-2 대비)
  - 비용 원칙: 흐림 면의 개수와 넓이를 줄인다. 360px 사이드 패널 전체에 live 흐림을 깔기보다 Mica 처럼 한 번 만든 바탕을 고정한다

---

## 7. 원리 요약 (우리 화면 규칙 후보)

1. 유리는 위층(떠 있는 툴바, 잠깐 뜨는 시트와 메뉴)에만. 코드 에디터, 메모, 카드 본문, 사이드 패널 바탕은 불투명 (Apple 콘텐츠 층 금지, Fluent 세로 패널은 불투명)
2. 유리 위에 유리를 올리지 않고, 한 화면의 live 흐림 면은 1~2개로 (Apple, Fluent, 흔한 꼴 목록)
3. 유리 위 글자는 지나갈 수 있는 최악의 바탕을 거친 색으로 4.5:1(큰 글자 3:1)을 잰다. 강조색 글자와 링크는 유리 위에 두지 않는다 (WCAG F83, Fluent)
4. `prefers-reduced-transparency: reduce` 와 `@supports not (backdrop-filter: none)` 에서는 불투명 바탕. Safari 는 미디어 쿼리를 못 받으니 앱 안 선택도 둔다
5. 빛과 흐림은 뜻 하나에만: 기억 확률. 장식용 후광, 네온 테두리, 격자 바탕, 글자 그라데이션은 쓰지 않는다
6. 기억 확률은 흐림 3~4단계로, 방향은 "흐릴수록 잊혀 감". 채도를 빼서 표현하지 않는다. 정확한 값은 글자로 함께 (MacEachren 2012, Kosara 2002, WCAG 1.4.11)
7. 흐림, 일렁임, 노이즈는 신호 그림에만 걸고 글자에는 걸지 않는다 (visionOS 글자 깊이 금지)
8. 저절로 5초 넘게 움직이는 일렁임은 멈출 수 있게 하고, `prefers-reduced-motion` 에서는 정지. 1초에 세 번 넘게 번쩍이지 않는다 (WCAG 2.2.2, 2.3.1)
9. 단계 경계는 목표 기억률(0.9) 기준, 밝기 단계는 OKLCH 의 L 로 고르게 나눈다
10. 화면마다 "지금 무슨 일인지" 한 문장 read 가 있어야 하고, 미래 고리는 하나만. 영화나 다른 제품의 겉모습을 옮기지 않는다 (Territory, Coleran, Perception)

---

## 조사하다 알게 된 것

- **ts-fsrs 6.0.0 이 이틀 전(2026-10-28) 나왔고 기본 모델이 FSRS-7 이다.** 기억 확률을 구하는 함수도 `scheduler.model.forgettingCurve(...)` 로 바뀌었다. ADR-0006 은 버전을 정하지 않았으니, 구현 때 버전(그리고 FSRS-6 / 7 중 무엇을 쓸지)을 정해야 한다. 공식 위키는 아직 FSRS-6 까지만 설명한다
- Fluent 문서가 **콘텐츠를 나누는 세로 패널은 불투명**하라고 한다. 우리 주 화면인 360px 크롬 사이드 패널이 정확히 그 경우다
- Mica 는 바탕 그림을 **한 번만** 샘플링해서 성능을 지킨다. 웹에서 "유리 느낌 바탕"을 live 흐림 없이 미리 만든 그림으로 내는 근거가 된다(web.dev 의 미리 흐린 그림 대체와 같은 방향)
- 흔히 "불확실성은 채도로"라고 하지만 실험에서는 채도가 가장 낮은 축에 속했다(MacEachren 2012). 투명도는 "쓸 만함"이다. 유리(투명도)와 흐림이 둘 다 "덜 확실함"으로 읽히니, 유리 패널 자체가 "덜 기억함"으로 오해되지 않게 신호와 재질을 구분해야 한다(우리 판단)
- 이 PC(Windows 11)의 "투명 효과" 설정 하나로 `prefers-reduced-transparency` 와 Fluent 대체 동작을 둘 다 시험할 수 있다

## 확인 못 한 것 (모음)

- Raycast, Arc 의 유리와 빛 사용에 대한 공식 설명
- Nothing 의 점 글자(Ndot) 공식 설명(공식 페이지가 열리지 않음)
- GMUNK 의 원칙(인터뷰 원문이 인증서 만료로 열리지 않음)
- Perception 의 "파란 선 이상", "빛이 아니라 물질" 발언 원문
- Cleveland, McGill 1984 원문의 순위 표, Heer, Bostock 2010 원문, Healey 의 preattentive 정리 페이지
- backdrop-filter 의 흐림 반경과 면적별 비용 숫자, `backdrop-filter: url()` 의 브라우저별 실제 지원
- Filter Effects 표준의 feDisplacementMap 제한 절 본문
- Apple 이 iOS 26 베타 중 투명도를 낮췄다는 보도의 원문

## 다음에 확인할 것

- 흐림 단계 3~4개가 360px 패널과 폰 카드 크기에서 실제로 구별되는지 (Kosara 제안처럼 최소, 최대 흐림을 직접 맞춰 보기)
- 사이드 패널에서 backdrop-filter 1~2면과 feTurbulence 정지 질감의 프레임 비용 (크롬 개발자 도구 Performance 패널)
- 폰 복습 카드를 어느 브라우저로 여는지에 따라 투명도 줄이기 대응 방식
