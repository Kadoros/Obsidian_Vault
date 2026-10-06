---
tags:
  - project
parent_concept:
---


Most neural operator research **targets** the large-data regime.
$\rightarrow$ Most neural operator research **focuses on** the large-data regime.
> [!NOTE] tip
> *(팁: 기존 연구 동향을 설명할 때는 'target' 같은 공격적인 단어 대신 'focuses on'으로 부드럽고 학술적인 톤을 유지할 것.)*



**We target** the opposite setting:
$\rightarrow$ **In contrast, we address** the opposite setting:
*(팁: 'In contrast'로 기존 연구와의 차별점을 극대화하고, 내 연구의 목표를 말할 때는 'address a problem'이라는 고급 동사를 쓸 것.)*

the opposite **setting**: the scientific **setting** where...
$\rightarrow$ the opposite **setting**: scientific **problems** where...
*(팁: 동일한 명사의 근접 반복을 피하고, 단순한 가상의 'setting'이 아니라 현실의 'problem'을 푼다는 실용성을 어필할 것.)*

Newton's forward difference **formula expresses** $a(x)$... / This **formula** is exact...
$\rightarrow$ Newton's forward difference **formula represents** $a(x)$... / This **representation** is exact...
*(팁: 기저(basis)를 이용해 함수를 나타낼 때는 단순한 공식(formula)이 아니라, 수학적으로 더 깊은 의미인 표현(representation)을 사용할 것.)*

...polynomials of degree **$\le m-1$**.
$\rightarrow$ ...polynomials of degree **at most** $m-1$.
*(팁: 문장 중간에 수학 기호(<=)를 문장 성분처럼 혼용하지 말고 영단어(at most)로 풀어서 쓸 것.)*

we **compute** monomial coefficients... via least-squares regression
$\rightarrow$ we **estimate** monomial coefficients... via least-squares regression
*(팁: 회귀분석, 최적화 등 오차가 동반되는 근사치를 구할 때는 'compute(계산)'가 아니라 'estimate(추정)'를 써서 오버클레임을 막을 것.)*

regression **(degree $d \ll m$)** on the sensor **values**, 
$\rightarrow$ regression **of degree $d \ll m$** on the sensor **observations**,
*(팁: 방법론의 핵심 전제조건(과결정계 등)은 괄호에 숨기지 말고 밖으로 뺄 것. 물리적 데이터는 value 대신 observation으로 쓸 것.)*

... we estimate monomial coefficients... **which avoids explicit Stirling number conversion and handles non-uniform sensor locations naturally.**
$\rightarrow$ **Rather than explicitly computing forward differences or converting between bases using Stirling numbers,** we estimate monomial coefficients... **This approach provides a numerically stable approximation while naturally extending to non-uniform sensor locations.**
*(팁: 1. 이론과 실제 구현이 다를 때는 'Rather than 이론, we do 구현'으로 의심을 사전 차단할 것. 2. 연산 과정을 피했다는 팩트보다 '수치적으로 안정적'이라는 강력한 장점(Benefit)을 포장할 것.)*

We fix d = 8 **with** over-determined least-squares, **avoiding** Runge's phenomenon.
$\rightarrow$ We fix d = 8 **and solve an** over-determined least-squares, which **improves numerical stability** and **mitigates** Runge's phenomenon.
*(팁: 수학 문제를 다룰 때는 전치사(with)로 뭉뚱그리지 말고 동작 동사(solve)를 쓸 것. 100% 장담할 수 없는 현상은 avoid 대신 mitigate(완화하다)로 방어할 것.)*

The approximation **error** satisfies $\|a - f_{\rm poly}\|_{L^2} = \dots$
$\rightarrow$ The **resulting** approximation satisfies $\|a - f_{\rm poly}\|_{L^2} = \dots$
*(팁: 수식 자체가 오차(error)를 의미할 때 주어에 또 error를 쓰면 논리적 중복이 됨. '우리가 구한 근사치가 이 오차식을 만족한다'로 쓸 것.)*

... confirms **GNR error is flat for** $d \in [5, 10]$.
$\rightarrow$ ... further shows that the **performance of GNR is relatively insensitive to the choice of** $d \in [5, 10]$.
*(팁: 하이퍼파라미터 안정성을 말할 때 'flat' 같은 구어체 대신 'insensitive to the choice of'라는 머신러닝 표준 표현을 쓰고 'relatively'로 뉘앙스를 조절할 것.)*

we embed $a$ into polynomial space
$\rightarrow$ we embed $a$ into **a** polynomial space
*(팁: 수학적 공간(space, set, manifold 등)을 지칭할 때는 추상적 개념이 아니라 우리가 정의한 '특정 공간'이므로 관사 a나 the를 반드시 붙일 것.)*

analysis **confirms GNR** error is...
$\rightarrow$ analysis **further shows that the** performance of GNR is...
*(팁: 실험 결과를 추가로 나열할 때는 confirms 보다 further shows that을 사용하여 '참고로 이런 부가적 장점도 있다'는 뉘앙스로 자연스럽게 연결할 것.)*

`\paragraph{1D Poisson}`
$\rightarrow$ `\noindent\textbf{1D Poisson}`
*(팁: 8페이지 제한이 빡빡한 학회 제출 시, 불필요한 상하 여백을 만드는 \paragraph 대신 \noindent\textbf를 활용해 시각적 구분과 공간 절약을 동시에 잡을 것.)*

Regression $f \approx \dots$, integrate twice apply boundary conditions:
$\rightarrow$ **We first approximate** $f$ **via polynomial** regression $f \approx \dots$, **and then obtain the solution by** integrating twice **while enforcing** boundary conditions:
*(팁: 방법론을 나열할 때는 메모(명사구) 형식을 버리고 'We first A, and then B' 형태의 완벽한 능동태 문장으로 서술할 것.)*

applying boundary conditions
$\rightarrow$ **enforcing** boundary conditions
*(팁: PDE나 물리 법칙에서 제약조건/경계조건을 시스템에 적용할 때는 apply 대신 'enforce'나 'impose'를 사용할 것.)*

(수식만 나열됨)
$\rightarrow$ **\emph{Intuition:}** A polynomial forcing term admits a closed-form solution... making the mapping... analytically tractable.
*(팁: 복잡한 수식이나 기법을 제시한 직후에는 반드시 'Intuition' 블록을 달아 이 수식이 왜 영리한 접근인지 그 통찰(Insight)을 독자에게 떠먹여 줄 것.)*

Fourier coefficients of $f_{\mathrm{poly}}$ computed analytically via...
$\rightarrow$ **We compute the** Fourier coefficients of $f_{\mathrm{poly}}$ analytically via...
*(팁: 파편화된 수동태 메모 형식을 완벽한 능동태 문장(We compute)으로 복구할 것.)*

... analytically via integration by parts, **then propagated** in time:
$\rightarrow$ ... analytically via integration by parts, **and propagate them** in time:
*(팁: 접속사 앞뒤의 문법적 병렬 구조(능동태-능동태)를 맞추고, 생략된 목적어(them)를 명시하여 독자의 뇌정지를 막을 것.)*

**Polynomial regression on** both $f$ and $a$ sensors.
$\rightarrow$ **We perform polynomial regression on** both $f$ and $a$ sensors.
*(팁: 명사구만 던져놓는 메모식 서술 금지. 완벽한 주어+동사 문장으로 쓸 것.)*

The Green's function $G(x,s)$ **(computed by FDM)**
$\rightarrow$ The Green's function $G(x,s)$ **is computed via a finite-difference method (FDM)**
*(팁: 약어(FDM)는 처음 나올 때 반드시 풀어쓰고, 중요한 행위 동사는 괄호 안에 가두지 말고 본문으로 꺼낼 것.)*

$<0.3\,$ms). $u_{\mathrm{GN}} = \int G\,f_{\mathrm{poly}}\,ds$ analytically.
$\rightarrow$ $<0.3\,$ms). **The solution is then obtained analytically as** $u_{\mathrm{GN}} = \dots$
*(팁: 중요한 최종 결과 수식 앞에는 'The solution is obtained as' 같은 안내 문구를 달아주고, 수식은 인라인(inline)이 아닌 독립된 수식 블록으로 빼서 강조할 것.)*

The solution is then `$u_{\mathrm{GN}} = \int G\,f_{\mathrm{poly}}\,ds$` **analytically.**
$\rightarrow$ The solution is then **obtained analytically as**
`\begin{equation}`
`u_{\mathrm{GN}} = \int G\,f_{\mathrm{poly}}\,ds.`
`\end{equation}`
*(팁: 부사(analytically)를 수식 뒤에 방치하지 말고 앞쪽 동사구로 묶을 것. 수식 끝에는 마침표를 찍을 것.)*

**Tensor**-product regression $f_{\mathrm{poly}} = \dots$, **Fourier sin sin** basis:
$\rightarrow$ **We apply t**ensor-product regression $f_{\mathrm{poly}} = \dots$ **and solve using the Fourier sine** basis:
*(팁: 'sin sin' 같은 조어 대신 정식 수학 명칭(the Fourier sine basis)을 쓰고, 관사(the)를 빼먹지 말 것. 문장은 능동태로 시작할 것.)*

(수식에서 $\hat{f}_{pq}$가 등장하지만 정의가 없음)
$\rightarrow$ 수식 바로 뒤에 **where $\hat{f}_{pq} = 4 \int_0^1 \int_0^1 f_{\mathrm{poly}}(x,y) \dots\,dx\,dy$.** 추가
*(팁: 수식에 새로운 변수나 기호가 등장했다면 직후에 반드시 정의(Define)하여 독자가 추측하게 만들지 말 것.)*

Fixed-point iteration:
$\rightarrow$ **We employ a** fixed-point iteration:
*(팁: 명사구만 남기지 말고 'We employ (우리는 ~을 채택했다)'라는 명확한 학술 동사로 문장을 완성할 것.)*

`x^{(k)} = x(x-1)\cdots(x-k+1)`**.**
$\rightarrow$ `x^{(k)} = x(x-1)\cdots(x-k+1)`**,**
**where $\Delta^k$ denotes the $k$-th forward difference operator.**
*(팁: 수식 블록 내에 설명 안 된 기호가 있다면 마침표 대신 쉼표로 연결하고 'where' 절로 정의할 것. 기호 정의에는 'denotes' 동사를 쓸 것.)*

(섹션 제목 직후 도입부 없이 바로 세부 설명 시작)
$\rightarrow$ **섹션 전체의 목적과 철학을 요약하는 도입부(Overview) 단락 추가:** We instantiate the GN prior for... allowing us to construct a physics-consistent baseline without training.
*(팁: 새로운 Section/Subsection을 시작할 때는 바로 본론으로 가지 말고, 1~2문장의 Overview로 "무엇을 보여줄 것인지", "이것이 우리 논문의 Contribution과 어떻게 연결되는지" 맵을 그려줄 것.)*


`u^{(k)} = \mathrm{GN}\!\left[f - \varepsilon\,(u^{(k-1)})^2\right]`**.**
$\rightarrow$ `u^{(k)} = \mathrm{GN}\!\left[f - \varepsilon\,(u^{(k-1)})^2\right]`**,**
**where GN denotes the Gregory-Newton embedding.**
*(팁: 앞서 $\Delta^k$를 정의할 때와 완벽히 동일한 패턴. 수식 내에서 자체적인 연산자(GN)를 정의하여 썼다면, 독자가 문맥으로 알 것이라 착각하지 말고 반드시 쉼표 + where 절 + denotes 동사로 명확히 정의할 것.)*

(섹션 제목 직후 도입부 없이 바로 Proposition 시작)
$\rightarrow$ **섹션 전체의 목적과 증명의 필요성을 설득하는 도입부(Overview) 단락 추가:** We analyze the theoretical properties... These results formalize how the analytic prior captures the underlying PDE structure and how...
*(팁: 이론(Theory) 섹션을 시작할 때는 곧바로 증명으로 넘어가지 말고, "이 수학적 증명들이 결국 우리 모델의 어떤 물리적/직관적 현상을 공식화(formalize)하는 것인지" 그 의미를 먼저 해설해 줄 것.)*

If $f$ is a polynomial of degree **$\le m-1$**,
$\rightarrow$ If $f$ is a polynomial of degree **at most $m-1$**,
*(팁: 문장 중간에 수학 기호(<=)를 문장 성분처럼 혼용하지 말고 영단어(at most)로 풀어서 쓸 것. - 반복 복습)*

For the heat equation, the same holds **with exact Fourier inner products.**
$\rightarrow$ For the heat equation, the same holds **when Fourier coefficients are computed exactly.**
*(팁: Theorem이나 Proposition에서 수학적 전제조건을 달 때는 모호한 명사구(with ~) 대신, 구체적인 행위와 조건이 담긴 절(when S + V)을 사용하여 빈틈을 없앨 것. 정확한 참값을 가정할 때는 compute 동사를 쓸 것.)*

`\noindent\emph{Implication.}` (단순 텍스트로 의미 전달)
$\rightarrow$ `\begin{tcolorbox}` ... **\textbf{Implication.} The GN prior exactly recovers...** `\end{tcolorbox}`
*(팁: Theorem이나 Proposition 직후에는 단순 텍스트가 아닌 눈에 띄는 '회색 박스(tcolorbox)'를 활용해 그 수학적 결과가 갖는 현실적/직관적 의미(Implication)를 리뷰어의 뇌리에 쾅 박아넣을 것.)*

Let $f \in H^s([0,1])$ and **$d \ll m$ fixed.** Then...
$\rightarrow$ Let $f \in H^s([0,1])$ and **fix $d \ll m$.** Then...
*(팁: 수학 명제에서 조건을 설정할 때는 명사 뒤에 'fixed'를 붙여 늘어지게 쓰지 말고, 'Let A and fix B' 처럼 명확하고 능동적인 명령 동사(Imperative verbs)를 사용할 것.)*

**(Proofs are provided in Appendix X.)**
$\rightarrow$ **Proofs are provided in Appendix X.**
*(팁: 증명이 부록에 있다는 안내 문구는 전체를 괄호로 감싸지 말고 당당한 독립 평서문으로 서술할 것.)*

**if** $\sup \dots \le M$ and $C\varepsilon < 1 \dots$ **, then**
$\rightarrow$ **assume** $\sup \dots \le M$ and $C\varepsilon < 1 \dots$ **. Then**
*(팁: 수학 명제에서 조건을 줄 때 if로 끌지 말고 'assume'이나 'let' 같은 능동적 명령문을 쓰고, 결론부는 마침표로 끊고 'Then'으로 시작할 것.)*

Under standard assumptions (e.g. Barron space residual**,** a two-layer $r_\theta$ with $W$ units**,** $n$ i.i.d. samples)
$\rightarrow$ Under standard assumptions (e.g. Barron space residual **and** a two-layer **network** with $W$ units **trained on** $n$ i.i.d. samples)
*(팁: 실험 세팅이나 조건을 나열할 때 콤마로 단어를 툭툭 던지지 말고, 'trained on'처럼 관계를 명확히 맺어주는 분사/전치사를 사용하여 서사(Context)를 만들 것.)*

with probability **$\ge$** $1-\delta$:
$\rightarrow$ with probability **at least** $1-\delta$:
*(팁: 문장 중간에 수학 기호(>=)를 문장 성분처럼 혼용하지 말고 영단어(at least)로 풀어서 쓸 것. - 3회차 복습)*

... the GNR requires **exponentially fewer** width units for the same accuracy **as DeepONet.**
$\rightarrow$ ... **the required network capacity is significantly reduced compared to learning the full operator directly.**
*(팁: 1. 'exponentially'처럼 극단적인 단어는 수학적 증명이 없다면 'significantly'로 낮출 것. 2. 경쟁 모델 이름을 직접 거론하며 깎아내리지 말고, 그 모델이 속한 '일반적인 방법론적 접근(learning the full operator directly)'을 언급하며 우회적으로 비판할 것.)*

**Since** $\|r\|_\gamma \ll \|\mathcal{G}\|_\gamma \dots$, the GNR requires **exponentially fewer** width units for the same accuracy **as DeepONet.**
$\rightarrow$ **Moreover, since** $\|r\|_\gamma \ll \|\mathcal{G}\|_\gamma \dots$, **the required network capacity is significantly reduced compared to learning the full operator directly.**
*(팁: 1. 앞선 증명이나 주장에 더하여 '결정적인 장점'을 하나 더 얹을 때는 'Moreover,' 같은 접속 부사로 논리의 상승 효과를 줄 것. 2. 경쟁 모델 직접 공격(DeepONet) 대신 방법론적 비판(learning the full operator)으로 우회하고, 과장된 단어(exponentially)를 학술적 단어(significantly)로 낮출 것 - 반복 복습)*

**(Proof in Appendix X.)**
$\rightarrow$ **Proofs are provided in Appendix X.**
*(팁: 증명 안내 문구는 괄호를 빼고 당당한 평서문으로 서술할 것 - 2회차 복습)*

(섹션 제목 직후 도입부 없이 바로 \begin{equation} 시작)
$\rightarrow$ **The proposed GNR decomposes the operator into a GN prior $u_{\mathrm{GN}}$ and a learnable residual $r_\theta$:**
$$\begin{equation}
\mathcal{G}_\theta(a)(y) = u_{\mathrm{GN}}(a)(y) + r_\theta(a, y).
\end{equation}$$
(팁: 수식은 맨몸으로 등장시키지 말고, 콜론(:)으로 끝나는 도입 문장으로 수식을 문장의 일부로 편입시킬 것. 이때 등장할 기호를 미리 호명해 두면 where 절 부담도 준다.)

$r_\theta$ **is a standard DeepONet residual network.** (앞 문장에서 이미 정의됨)
$\rightarrow$ (삭제)
*(팁: 바로 앞에서 denotes로 정의한 대상을 다시 설명하지 말 것.)*

`\begin{itemize}` (예고 없이 리스트 시작)
$\rightarrow$ **We consider two configurations:**
`\begin{itemize}`
*(팁: 리스트도 수식과 같다. 맨몸으로 시작하지 말고 개수를 못 박은 도입 문장을 앞에 둘 것.)*

\item \emph{GNR-same}**: identical architecture to** baseline DeepONet
$\rightarrow$ \item \emph{GNR-same}**, which uses the same architecture as the** baseline DeepONet
*(팁: 리스트 항목도 콜론+명사구 메모를 버리고 which 관계절로 문장화할 것. identical은 완전 동일을 주장하므로 the same as로 낮출 것.)*


\item \emph{GNR-small}**: $3\times$** fewer parameters
$\rightarrow$ \item \emph{GNR-small}**, which uses approximately $3\times$** fewer parameters
*(팁: 2.2k/0.7k는 정확히 3배가 아니다. 반올림한 배수 앞에는 approximately를 붙일 것.)*

**Training objective:** $\min_\theta \mathbb{E}[\dots]$**.** (인라인 수식)
$\rightarrow$ **The model is trained by minimizing**
\begin{equation}
$$\min_\theta \,\mathbb{E}\big[\|r_\theta(a,y) - (u_{\mathrm{exact}}(a)(y) - u_{\mathrm{GN}}(a)(y))\|^2\big],$$
\end{equation}
*(팁: 핵심 수식을 콜론+명사구 라벨과 함께 인라인에 방치하지 말 것. 라벨은 완전한 문장으로 승격시키고 수식은 독립 블록으로 뺄 것. 뒤로 이어지는 수식의 끝은 마침표가 아니라 쉼표.)*

$\min_\theta \mathbb{E}[\|$**$r_\theta$** $-$ ($u_{\mathrm{exact}}$ $-$ $u_{\mathrm{GN}}$)$\|^2]$
$\rightarrow$ $\min_\theta \mathbb{E}[\|$**$r_\theta(a, y)$** $-$ ($u_{\mathrm{exact}}$**$(a)(y)$** $-$ $u_{\mathrm{GN}}$**$(a)(y)$**)$\|^2]$
*(팁: 앞서 정의한 수식과 같은 기호를 다시 쓸 때는 인수까지 똑같이 채워 표기를 통일할 것. 두 수식이 눈으로 대응돼야 독자가 연결한다.)*

(섹션이 설명 문장으로 끝나고 그림 참조 없음)
$\rightarrow$ **Figure~\ref{fig:pipeline} illustrates the overall pipeline of the proposed GNR.**
*(팁: 그림을 넣었으면 반드시 본문에서 \ref로 호명할 것. 섹션 끝에 배치하면 마무리 역할까지 한다.)*


(수식 (10) 직후 해설 없이 바로 다음 주장으로 넘어감)
$\rightarrow$ **i.e., the residual network learns only the discrepancy between the GN prior and the exact solution.**
*(팁: 수식을 던졌으면 바로 뒤에 i.e.로 그 수식이 말로 무슨 뜻인지 한 번 풀어줄 것.)*

**The residual** targets only the GN approximation error
$\rightarrow$ **the residual network learns** only the discrepancy
*(팁: 학습의 주체는 잔차(residual)가 아니라 잔차망(residual network)이다. 주어를 정확히 고를 것.)*

The residual targets only the GN approximation error, **which is zero** for polynomial inputs **and $\mathcal{O}(h^s)$** otherwise.
$\rightarrow$ **Since the GN prior is exact** for polynomial inputs **and incurs an error of $\mathcal{O}(h^s)$** otherwise, **the residual term is significantly simpler than learning the full operator.**
*(팁: 사실 나열로 끝내지 말고 Since A, B로 전제→결론 논증을 만들 것. 오차가 0이라는 부정 표현은 prior가 exact하다는 긍정 프레이밍으로 바꾸고, 동사 없는 파편($\mathcal{O}(h^s)$)에는 incurs an error of로 동사를 채울 것.)*

**The GN prior** requires no gradient computation at **inference**.
$\rightarrow$ **Moreover, the GN prior is analytic and** requires no gradient computation at **inference time**.
*(팁: 장점을 하나 더 얹을 때는 Moreover로 연결하고, 원인(analytic)과 결과(no gradient)를 and로 한 문장에 묶을 것.)*

**Figure**~\ref{fig:pipeline}
$\rightarrow$ **Fig.**~\ref{fig:pipeline}
*(팁: 지면이 빡빡하면 Figure는 Fig.로 줄일 것.)*

**i.e.,** the residual network learns...
$\rightarrow$ **\ie** the residual network learns...
*(팁: i.e., e.g., et al., cf.는 직접 타이핑하지 말고 \ie, \eg 매크로로 쓸 것. 마침표를 문장 끝으로 오인해 간격이 벌어지는 것을 막고, 표기도 논문 전체에서 자동 통일된다.)*

\textbf{Poisson}: both... / \textbf{GNR leads consistently from $n=10$}.
$\rightarrow$ \emph{Poisson}: both... / \emph{GNR leads consistently from $n=10$}.
*(팁: 산문 속 강조는 \textbf(굵게)가 아니라 \emph(이탤릭)가 학술 표준. bold는 표 안 최고 수치 정도로 아껴 쓸 것.)*

\subsection{Main Results}
**\subsection**{1D Poisson: Full Baseline Comparison}
$\rightarrow$ \subsection{Main Results}
**\noindent\textbf**{1D Poisson: Full Baseline Comparison**.**}
*(팁: \subsection 바로 밑에 또 \subsection을 쓰면 계층이 뭉개진다. 하위 소제목은 \noindent\textbf로 격하해 계층 정리와 여백 절약을 동시에 할 것. 인라인 소제목 끝에는 마침표를 찍어 본문과 끊어줄 것.)*

\centering
**\small**
$\rightarrow$ \centering
**\scriptsize**
*(팁: 표가 페이지 폭이나 높이를 넘으면 폰트 크기를 한 단계 더 낮출 것. \small → \scriptsize.)*

\noindent\textbf{1D Poisson: Full Baseline Comparison.}
$\rightarrow$ \noindent\textbf{1D Poisson: Full Baseline Comparison **(Table \ref{tab:poisson})**.}
*(팁: 소제목에서 다룰 표/그림을 \ref로 바로 호명하면 독자가 제목만 보고 대상을 안다.)*

(소제목 직후 해설 없이 바로 \begin{table})
$\rightarrow$ **GNR consistently outperforms both DON and PI-DON in low-data regimes ($n \ge 10$), achieving up to $4.3\times$ lower error. Notably, PI-DON underperforms DON across all settings, suggesting that physics-based regularization alone may be insufficient when supervision is limited. These results indicate that incorporating analytic structure via the GN prior provides a more effective inductive bias than penalty-based approaches.**
*(팁: 표를 맨몸으로 던지지 말 것. 앞에 해설 단락을 두되 "수치 요약 → Notably+관찰/suggesting 해석 → These results indicate 의미 격상" 순으로 표를 주장으로 번역할 것.)*

...approaches.**\label{sec:exp1}** (문단 끝에 붙음)
$\rightarrow$ ...approaches. (삭제; \label은 \subsection 바로 뒤로)
*(팁: \label은 \section/\subsection 명령 바로 뒤에 붙여야 그 번호를 정확히 참조한다. 문단 중간·끝에 두지 말 것.)*

\begin{table}[H]
\caption{...}
\label{tab:poisson}
$\rightarrow$ \begin{table}[H]
**\vspace{-2mm}**
\caption{...}
\label{tab:poisson}
**\vspace{-2mm}**
*(팁: 지면이 빡빡하면 \begin{table} 직후와 \label 직후에 \vspace{-2mm}로 표 주변 여백을 짜낼 것.)*


(표 강조 규칙)
*(팁: 표에서 bold는 각 행의 실제 1등, underline은 2등/baseline 최고로 역할을 분리할 것. 내 방법이 진 칸(n=5)에서는 경쟁자에게 정직하게 bold를 양보하고, 그 패배는 본문에서 정당화할 것. 표를 조작하지 않는 정직함이 리뷰어 신뢰를 만든다.)*

(표 캡션 작성)
*(팁: 캡션만 읽어도 표가 독립적으로 이해되게 쓸 것 — 좌우 구성, 하이퍼파라미터, prior floor 수치, seed 수, 지표 정의(relative L² error, mean±std)까지. 이 표에서 뺀 baseline(PI-DON)은 "in Appendix D.11"로 위치를 미리 안내해 누락 의심을 차단할 것.)*

(표 안에 \small\textit{...}로 해설 각주를 우겨넣음)
$\rightarrow$ (삭제 — 그 내용은 본문 해설 단락으로 이동)
*(팁: 표 내부에 산문 해설을 넣지 말 것. 해설은 표 앞 본문 단락에 완전한 문장으로 빼고, 표 안에는 데이터만 남길 것.)*

(표 처리 템플릿 — 모든 표에 동일 적용)
*(팁: 표마다 반복할 것 — ① \noindent\textbf{제목 (Table \ref{...}).} ② 수치→suggest that 해석→의미 순의 본문 해설 단락 ③ \begin{table}[H] 직후 \vspace{-2mm} ④ prior floor·seed 넣은 \caption + \label ⑤ \vspace{-2mm} + \scriptsize. 교정은 일회성이 아니라 재사용 템플릿으로 만들 것.)*

(Variable-Coefficient 표 소제목 + 해설)
$\rightarrow$ \noindent\textbf{Variable-Coefficient: Fair FDM Comparison (Table \ref{tab:vc}).}
**While FDM-DON benefits from access to numerical priors, GNR achieves significantly better performance across all sample sizes. This demonstrates that the performance gain is not solely due to access to discretization information, but rather from the structured analytic prior provided by the GN formulation.**
*(팁: "네가 이긴 건 정보를 더 받아서 아니냐"는 공정성 공격은, 경쟁자에게 같은 정보를 준 뒤(Fair) 그래도 이겼음을 보이고 "not solely due to A, but rather from B" 구문으로 승리 원인을 정보 접근이 아닌 구조로 못박아 방어할 것.)*


\centering
$\rightarrow$ \centering
**\setlength{\tabcolsep}{20pt}**
**\renewcommand{\arraystretch}{0.7}**
*(팁: 표 미세조정 — \tabcolsep은 열 간격(키우면 좁은 표가 페이지 폭을 채움), \arraystretch는 행 높이 배율(0.7로 줄이면 세로 압축). 가로로 벌려 보기 좋게, 세로로 줄여 지면 절약. 이 줄을 넣으면 근처 \vspace는 중복이니 정리할 것.)*

(표 안 \small\textit{...} 해설 메모)
$\rightarrow$ %\small\textit{...} (삭제가 아니라 % 주석 처리)
*(팁: 표 안 메모를 본문으로 옮겼을 때, 완전히 버릴 게 아니라 "이 표의 핵심 메시지"라는 근거로 남기고 싶으면 삭제 대신 %로 주석 처리해 소스에 흔적을 남길 것.)*

(2D Poisson — 개선폭이 작은 표의 해설)
$\rightarrow$ **GNR consistently improves over DON across all sample sizes, with moderate but stable gains. This suggests that the GN prior extends effectively to higher-dimensional settings, although the relative improvement is smaller due to increased problem complexity.**
*(팁: 결과가 약할 때는 감추지 말 것. "moderate"로 솔직히 인정하고, "although ... due to increased problem complexity"로 왜 약한지 이유를 먼저 대서 리뷰어의 지적을 선점할 것. 신뢰는 전승이 아니라 "질 때 이유를 아는 것"에서 나온다.)*

(Mildly Nonlinear 표 — n=5 방어)
$\rightarrow$ **At very small sample sizes ($n=5$), performance is comparable, likely because the GN prior error is already small relative to the available supervision.**
*(팁: "low-data가 강점인데 왜 최소 n에서 안 이기냐"는 공격을 선점하는 문장. comparable로 정직하게 인정하고, 실험으로 확증 못 한 해석은 because가 아니라 "likely because"로 톤을 낮춰 오버클레임을 막을 것.)*

(논문 전체 방어 일관성)
*(팁: 같은 약점(n=5 미지근함)을 표마다 같은 뿌리 논리 — "prior가 이미 정확해 residual이 배울 게 없다" — 로 변주해 반복 방어할 것. 방어막이 논문 전체에서 일관되면 리뷰어가 어느 표를 찔러도 같은 대답이 나와 뚫리지 않는다.)*


\textbf{Comparison of the proposed **GN-Operator GNR and vs** baseline methods...}
$\rightarrow$ \textbf{Comparison of the proposed **GNR** baseline methods...}
*(팁: 캡션에서 풀네임(GN-Operator)과 약칭(GNR)을 겹쳐 쓰지 말 것. 논문에서 통일한 약칭 하나만. and/vs 같은 중복 접속사도 정리.)*

(a) GNR **leads** from n=10.
$\rightarrow$ (a) **\emph{1D Poisson:}** GNR consistently **outperforms baseline** from n=10.
*(팁: 다중 패널 그림은 각 패널에 \emph{라벨:}을 달아 캡션만으로 구조가 보이게 할 것. lead 같은 막연한 동사는 outperform+목적어(baseline)로 대상을 명확히.)*

(b) GNR achieves 5.3~5.9× **improvement** at n=10~50.
$\rightarrow$ (b) \emph{Heat equation:} GNR achieves 5.3–5.9× **lower error** for n=10–50.
*(팁: "improvement"는 무슨 개선인지 모호하다. 측정 지표(lower error)로 바꿔 정확히 명시할 것.)*

(d) \emph{achieves >17× improvement throughout.} (내용 오류: (c)와 중복)
$\rightarrow$ (d) \emph{Convergence at n=20:} GNR starts from a 36.3% error (GN prior, zero training), while DeepONet reaches 61.6% after 400 training epochs.
*(팁: 패널 설명이 실제 그림 내용과 맞는지 확인할 것. 수렴 그래프면 "zero training vs 400 epochs"를 while로 대비시켜 학습 없이 이긴다는 핵심을 한 문장에 담을 것.)*

(그림 캡션 원칙)
*(팁: 그림 캡션은 그림을 대신 읽어주는 미니 문단이다. 패널마다 \emph{라벨:} + 무엇을 보여주는지 + 정확한 핵심 수치. 본문 없이 그림만 봐도 완결되게. 캡션 숫자는 반드시 본문 표와 대조해 일치시킬 것.)*

\subsection{Main Results}
**\noindent\textbf{1D Poisson...}** (Overview 없이 첫 소제목으로 직행)
$\rightarrow$ \subsection{Main Results}
**As shown in Figure~\ref{fig:main}, GNR consistently outperforms baseline methods across multiple benchmarks and exhibits faster convergence, starting from a strong analytic prior even without training.**
\noindent\textbf{1D Poisson...}
*(팁: 세부 소제목으로 직행하지 말고 섹션 Overview 한 문장을 먼저 둘 것. ① 섹션 전체 결론을 미리 요약(숲 먼저) ② 대표 Figure를 \ref로 호명 ③ 논문 핵심 셀링포인트를 결과 섹션 첫 문장에 박기. "이 섹션이 결국 뭘 말하나?"에 먼저 답하는 문장.)*


(문서 구조 — 블록 배치 순서)
[Figure 2: 메인 결과]
**[Figure 3: 비용/외삽 — semiconductor 내용]**  ← 5장 초입에 misplaced
[실험 세팅 문단]
$\rightarrow$ Figure 3을 이 위치에서 삭제하고 semiconductor 섹션(6장)으로 이동
*(팁: 문장뿐 아니라 그림·표·문단의 "배치 순서"도 독자의 이해 순서를 따라야 한다. ① 실험 세팅을 설명하기 전에 결과 그림을 먼저 쏟지 말 것 ② 특정 케이스(semiconductor)를 위한 그림은 그 케이스를 다루는 섹션에 둘 것. LaTeX 플로팅으로 그림이 엉뚱한 데 뜨면 소스 위치 자체를 옮겨 바로잡을 것.)*


(메인 결과 섹션 직후, 엉뚱한 곳에 있던 그림을 끌어오거나 새로 삽입함)
$\rightarrow$ **`\begin{figure}[t]`**
**`...`**
**`\caption{\textbf{Cost-accuracy tradeoff and extrapolation.} (a) GNR achieves less than 10\% error at $n=3$ (approximately \$3,000), while DeepONet does not reach 10\% error even with substantially higher cost (up to \$50,000)...}`**
*(팁: 논문의 가장 강력한 무기(예: 압도적인 비용 절감, 일반화 능력)를 보여주는 그림은 뒤로 미루지 말고 메인 결과 직후에 전진 배치할 것. 캡션은 단순한 '그림 설명'이 아니라 "우리는 3천 불에 되는데 쟤네는 5만 불 써도 안 된다"처럼 구체적 수치를 대비시키는 '스토리텔링'으로 작성하여 리뷰어를 설득할 것.)*

`\subsection{Noise Robustness and Inference Time}`
**`\begin{table}[H]`** (Overview 없이 바로 표로 직행)
$\rightarrow$ `\subsection{Noise Robustness and Inference Time}`
**`As shown in Table~\ref{tab:noise}, GNR consistently outperforms... This robustness can be attributed to the polynomial embedding, which acts as an implicit low-pass filter and suppresses high-frequency noise...`**
`\begin{table}[H]`
*(팁: 새로운 섹션이나 표를 시작할 때 맨몸으로 던지지 말고 반드시 해설 단락을 먼저 둘 것. 특히 성능이 좋게 나온 경우, 단순히 "이겼다"로 끝내지 말고 "이 결과는 우리 모델의 어떤 구조적 특징(예: low-pass filter 역할) 덕분이다"라는 물리적/수학적 통찰(Insight)을 덧붙여 리뷰어의 의구심을 원천 차단할 것.)*

`\begin{table}[H]`
`...`
**`\small`**
$\rightarrow$ `\begin{table}[H]`
`...`
**`\centering`**
**`\setlength{\tabcolsep}{20pt}`**
**`\renewcommand{\arraystretch}{0.7}`**
**`\scriptsize`**
*(팁: 학회 논문 지면 쥐어짜기 템플릿. 열 개수가 적어 표가 좁아 보일 때는 `\tabcolsep`을 키워 가로로 시원하게 벌리고, 세로 공간을 아끼려면 `\arraystretch`를 0.7 정도로 줄여 행 높이를 납작하게 압축할 것. 폰트도 `\small` 대신 `\scriptsize`로 한 단계 더 낮춰 공간을 확보할 것.)*



`\small\textit{$\ge2.4\times$ advantage up to SNR=10. LSTSQ polynomial prior acts as low-pass filter.}`
$\rightarrow$ **`%\small\textit{$\ge2.4\times$ advantage up to SNR=10. LSTSQ polynomial prior acts as low-pass filter.}`**
*(팁: 표 안에 산문 형태의 해설이나 결론을 넣지 마라. 해설은 표 앞의 본문 단락으로 빼서 완전한 문장으로 서술할 것. 단, 소스코드에서 완전히 지우지 말고 `%`로 주석 처리해 두면, 나중에 수정할 때 "이 표가 증명하려던 핵심 메시지"를 잊지 않는 좋은 이정표가 된다.)*


`Table~\ref{tab:time} reports the per-sample inference time of each method.` (단순 사실 나열)
$\rightarrow$ `Table~\ref{tab:time} reports the per-sample inference time of each method.` **`While GNR introduces additional overhead due to the analytic prior, the absolute cost remains below $0.25$ ms per sample. This indicates that the proposed method achieves improved accuracy with a modest increase in computational cost.`**
*(팁: 내 모델이 경쟁 모델보다 속도가 느리거나 메모리를 더 쓰는 등 명백한 단점이 있다면, 리뷰어가 지적하기 전에 "While ~ (비록 ~하긴 하지만)" 구문으로 먼저 매를 맞아라. 단점을 스스로 인정한 직후, "절대적인 수치 자체는 미미하다(remains below ~)"라고 방어하고, "약간의 비용 증가로 큰 성능 향상을 얻었다(modest increase)"라며 훌륭한 가성비(Trade-off)로 포장해버려라. 약점을 숨기다 들키면 리젝이지만, 스스로 분석하고 정당화하면 신뢰를 얻는다.)*



`We evaluated the proposed method on five PDE` **`\begin{figure}[t] ... \end{figure}`** `benchmarks:`
$\rightarrow$ **`We evaluated the proposed method on five PDE benchmarks:`** (Figure 블록은 문단 밖으로 이동)
*(팁: LaTeX 소스코드를 작성할 때, `\begin{figure}` 블록을 문장이나 문단 한가운데에 삽입하지 마라. 렌더링 결과와 상관없이 소스코드의 가독성을 심각하게 해친다. 그림 블록은 반드시 문단이 끝난 후나 섹션의 시작/끝 등 논리적으로 독립된 위치에 배치할 것.)*


`Five benchmarks: (1) 1D Poisson. (2) Heat equation...`
$\rightarrow$ **`We evaluated the proposed method (GNR) on five PDE benchmarks: (1) 1D Poisson; (2) the heat equation...`**
`Sources: 50% polynomial and 50% sinusoidal.`
$\rightarrow$ **`The source terms consist of 50% polynomial and 50% sinusoidal components.`**
`Sensors: m=11 (1D), 25 (2D).`
$\rightarrow$ **`We used m=11 sensors for 1D problems and a 5x5 grid (25 sensors) for 2D.`**
*(팁: 실험 세팅(데이터셋, 하이퍼파라미터 등)을 설명할 때 `명사: 값` 형태의 메모장식 나열을 절대 피하라. 반드시 `We evaluated...`, `The source terms consist of...`, `We used...` 처럼 주어와 동사를 갖춘 완벽한 문장(Full sentence)으로 서술할 것. 여러 항목을 나열할 때는 마침표로 툭툭 끊지 말고 세미콜론(`;`)과 `and`를 사용해 부드럽게 연결하라.)*


`Dirichlet BC` $\rightarrow$ **`Dirichlet boundary conditions`**
`Nonlinear Poisson equation` $\rightarrow$ **`mildly nonlinear Poisson equation`**
*(팁: 본문 줄글 내에서는 `BC` 같은 약어를 쓰지 말고 `boundary conditions`처럼 정식 명칭으로 풀어서 쓸 것. 또한, 수식이나 조건에 제한이 있다면(예: $\varepsilon \le 0.5$), 단순히 'Nonlinear'라고 뭉뚱그리지 말고 'mildly nonlinear(약한 비선형)'처럼 정확한 수식어를 붙여 오버클레임을 방지할 것.)*


`Baselines: DeepONet, PI-DeepONet...`
$\rightarrow$ **`We compared against standard baselines including DeepONet, PI-DeepONet...`**
`Training: 400 epochs using lr=4e-3.`
$\rightarrow$ **`All models were trained for 400 epochs using cosine-annealed Adam with a learning rate of 4e-3.`**
`Test: 200 held-out test pairs.`
$\rightarrow$ **`Evaluation was performed on 200 held-out test pairs.`**
*(팁: 실험 세팅을 적을 때 `항목: 내용` 식의 메모장 스타일을 절대 쓰지 마라. `We compared against...`, `All models were trained for...`, `Evaluation was performed on...` 처럼 수동태/능동태를 적절히 섞어 완벽한 문장으로 서술할 것. 괄호 안의 부연 설명도 기호 나열이 아닌 영어 구문(`with PDE residual weight...`)으로 다듬어라.)*

`GNR-same: identical params to DON.`
$\rightarrow$ **`For fair comparison, \emph{GNR-same} used the same architecture and parameter count as DeepONet.`**
*(팁: 베이스라인과 내 모델의 크기를 맞췄다는 사실을 적을 때는 단순히 "파라미터가 같다"라고만 쓰지 말고, 문장 맨 앞에 `For fair comparison`을 붙여 리뷰어에게 "우리는 꼼수를 쓰지 않고 공정하게 비교했다"는 인상을 강하게 심어주어라.)*

`FNO excluded: requires uniform grid and $n \ge 1000$ samples.`
$\rightarrow$ **`\emph{FNO was excluded}, as it requires a fixed uniform grid and a large number of labeled samples ($n \ge 1,000$) \cite{li2021}, both of which are incompatible with our setting.`**
*(팁: 분야에서 유명한 모델을 실험에서 뺐다면 리뷰어의 1순위 공격 대상이 된다. 배제할 때는 단순히 "안 썼다"가 아니라, "그 모델은 A와 B를 요구하는데, 이는 우리의 문제 설정과 근본적으로 양립할 수 없다(incompatible)"라고 논리적으로 방어하라. 해당 모델의 논문을 인용(`\cite`)하여 내 주장이 팩트임을 뒷받침하는 것도 잊지 말 것.)*


`\emph{Behavior at n=5.}`
$\rightarrow$ **`\noindent\textbf{Behavior at n=5.}`**
*(팁: 문단 맨 앞에서 소제목 역할을 하는 텍스트는 이탤릭체(`\emph`) 대신 굵은 글씨(`\noindent\textbf`)를 사용하여 본문과 시각적으로 명확히 분리할 것.)*


`For Poisson, both DON and GNR are unstable because the residual target is too small.`
$\rightarrow$ **`For \emph{Poisson}, both DON and GNR exhibit high variance, as the GN prior is nearly exact, leaving the residual target too small to learn reliably.`**
`For Heat equation, GNR wins because the residual is large enough to learn.`
$\rightarrow$ **`For the \emph{heat equation}, GNR outperforms DON, since the residual error remains sufficiently large for effective learning.`**
`For Nonlinear case, DON wins because error is too small for 5 samples.`
$\rightarrow$ **`For the \emph{nonlinear} case, DON performs better, as the fixed-point GN prior already yields a small error, again limiting the learnable signal.`**
*(팁: 내 모델이 특정 조건에서 지거나 성능이 불안정할 때, `unstable`, `wins`, `too small` 같은 구어체나 단순한 표현을 쓰지 마라. `exhibit high variance`, `outperforms`, `limiting the learnable signal` 같은 학술적 용어로 격상시켜라. 특히 내가 진 이유를 설명할 때도 "우리가 못해서"가 아니라 "우리 prior가 이미 너무 정확해서(nearly exact) 네트워크가 배울 신호가 부족했다(limiting the learnable signal)"라는 식으로, 약점을 강점의 부작용으로 포장하는 논리를 구축하라.)*


`In all cases, GNR leads consistently from n=10.`
$\rightarrow$ **`Overall, GNR becomes consistently advantageous from $n \ge 10$ across all settings.`**
*(팁: 여러 케이스를 종합하여 결론을 내릴 때 `In all cases`나 `leads` 같은 투박한 표현 대신, `Overall`과 `becomes consistently advantageous across all settings`처럼 부드럽고 포괄적인 학술 표현을 사용할 것.)*


(본문에 그림에 대한 언급이 누락되어 있던 상태)
$\rightarrow$ **`As illustrated in Fig.\ref{fig:cost_extrap}, GNR achieves less than 10\% error at significantly lower cost compared to DeepONet, and further demonstrates strong generalization to unseen HfO$_2$ configurations.`**
*(팁: 논문에 그림이나 표를 넣었다면 본문에서 반드시 `\ref`로 호명해야 한다(고아 그림 방지). 이때 단순히 "Figure X를 참조하라"고 쓰지 마라. "Figure X에서 보듯이, 우리 모델은 A라는 압도적인 장점이 있고 B라는 능력까지 증명했다"처럼, 리뷰어가 그림을 보고 내려야 할 '결론'을 저자가 직접 문장으로 완성해서 입에 떠먹여 주어라.)*



(그림만 덜렁 넣거나 단순 제목만 적음)
$\rightarrow$ **`\caption{\textbf{Robustness analysis.} (a)~\emph{Model mismatch:} the residual network effectively improves upon the analytic GN prior, reducing error beyond the 13.1\% baseline. (b)~\emph{Degree sensitivity:} GNR performance remains stable...}`**
*(팁: 여러 패널로 구성된 그림의 캡션은 반드시 `(a) \emph{라벨:}` 형태로 각 패널을 명확히 구분하라. 그리고 단순히 "무엇을 그린 그래프인지" 설명하지 말고, "이 그래프를 통해 증명된 구체적인 수치와 결론(예: 13.1% 베이스라인을 넘어 에러를 줄인다)"을 캡션에 직접 적어 리뷰어에게 결론을 떠먹여라.)*


`\subsection{Robustness Analysis}`
`\textbf{(a) Model mismatch.}` (바로 세부 항목으로 직행)
$\rightarrow$ `\subsection{Robustness Analysis}`
**`As illustrated in Fig.\ref{fig:robustness}, GNR remains robust under model mismatch, is largely insensitive to the choice of polynomial degree, and consistently outperforms DON under irregular sensor placements.`**
`\textbf{(a) Model mismatch.}`
*(팁: 새로운 섹션을 시작할 때 세부 소제목으로 바로 들어가지 마라. 반드시 그 섹션 전체의 결론을 요약하는 한 문장(Overview)을 먼저 배치하여 독자에게 '숲'을 먼저 보여주어라.)*


`when the GN prior uses the linear Poisson... but data include unknown physics`
$\rightarrow$ **`where the GN prior assumes a linear Poisson... while the data include additional nonlinear radiation effects`**
`GNR breaks through from n=5... as the residual network learns the unknown physics.`
$\rightarrow$ **`GNR improves upon this baseline starting from n=5... indicating that the residual network effectively captures the missing physics.`**
*(팁: 논문을 쓸 때 흥분해서 문학적이거나 과장된 표현을 쓰지 마라. `uses` $\rightarrow$ `assumes`, `unknown physics` $\rightarrow$ `additional nonlinear effects` / `missing physics`, `breaks through` $\rightarrow$ `improves upon`, `learns` $\rightarrow$ `captures`처럼 차분하고 객관적인 학술 동사와 명사로 톤다운시켜라. 오버클레임은 리뷰어의 공격 본능을 자극할 뿐이다.)*


`GNR performance is flat... confirming $d$ is not a critical hyperparameter.`
$\rightarrow$ **`GNR performance remains stable... suggesting that the method is not highly sensitive to this hyperparameter.`**
*(팁: 실험 결과 하나로 어떤 사실을 100% '확증(confirm)'한다고 단정 짓지 마라. 리뷰어는 예외 상황을 찾아내 공격하려 든다. `confirming` 대신 `suggesting(시사한다)`이나 `indicating(나타낸다)`으로 한 발 물러서고, `not critical` 같은 극단적 표현 대신 `not highly sensitive(크게 민감하지 않다)`처럼 부드러운 학술 언어로 방어막을 쳐라.)*


`... with $\pm 50\%$ jitter on sensor locations. GNR still outperforms DON by $2.0\times$ with essentially flat error...`
$\rightarrow$ **`We further evaluated robustness to irregular sensor placement by introducing up to $\pm 50\%$ jitter in sensor locations. GNR maintains a consistent advantage over DON (approximately $2.0\times$) across all jitter levels, with minimal variation in error, indicating robustness to non-uniform sampling.`**
*(팁: 실험 세팅을 설명할 때 전치사(`with`)로 대충 얼버무리지 말고, "우리가 어떤 목적을 위해 어떤 조작을 가했다(`We evaluated... by introducing...`)"라고 명확한 문장으로 써라. 또한, 결과를 서술할 때 수치만 나열하지 말고, 문장 끝에 `indicating...`을 붙여 "이 수치가 결국 물리적/수학적으로 어떤 의미(예: 비균일 샘플링에 대한 강건성)를 갖는지" 리뷰어에게 직접 해석해 주어라.)*

`The ratio reaches up to $401\times$, leading to a severely discontinuous problem.`
$\rightarrow$ **`The resulting conductivity contrast reaches up to $401\times$, leading to a highly discontinuous variable-coefficient problem.`**
*(팁: 내가 푸는 문제가 얼마나 어려운지 설명할 때 `severely` 같은 감정적 단어는 피하고 `highly` 같은 객관적 단어를 써라. 또한 `ratio`보다는 `contrast(대비)`처럼 물리적 차이를 극대화하는 어휘를 선택하여, "이렇게 어려운 문제(highly discontinuous)를 우리 모델이 풀어냈다"는 뉘앙스를 깔아두어라.)*

`GNR exploits $k(x)$ exactly; whereas DeepONet infers $k(x)$'s effect implicitly from data.`
$\rightarrow$ **`In this setting, GNR explicitly incorporates $k(x)$ by computing the Green's function $G(x,s;\,k)$, whereas DeepONet must implicitly learn the effect of $k(x)$ from data.`**
*(팁: 내 모델이 경쟁 모델을 이긴 이유를 설명할 때, 단순히 "우리가 더 잘 쓴다"라고 하지 마라. "우리는 A라는 수학적 방법(Green's function)을 통해 물리 법칙을 명시적으로(explicitly) 통합하지만, 경쟁 모델은 데이터로부터 암묵적으로(implicitly) 학습해야만 한다(must)"라고 구조적 한계를 찔러라. `explicitly`와 `implicitly`의 대비는 리뷰어를 설득하는 아주 강력한 무기다.)*

(표를 바로 제시함)
$\rightarrow$ **`Table~\ref{tab:semi_main} reports... GNR consistently outperforms all baselines... achieving up to $30\times$ lower error. ... PI-DeepONet fails to provide gains despite access to exact $k(x)$, likely due to instability introduced by the large conductivity discontinuity. These results highlight the advantage of explicitly incorporating the PDE structure via the GN prior...`**
*(팁: 메인 결과 표를 보여주기 전에 반드시 해설 단락을 써라. 이때 내 모델의 수치적 우수성만 자랑하지 말고, 경쟁 모델(예: PI-DeepONet)이 왜 실패했는지 그 물리적/수학적 원인(예: 불연속성으로 인한 불안정성)을 분석해 주어라. 단, 100% 확신할 수 없는 원인 분석에는 `likely due to(~때문일 것이다)`를 붙여 오버클레임을 방지하라. 마지막 문장은 `These results highlight...`로 시작하여 이 표가 증명하는 최종 결론(Insight)을 쐐기 박듯 적어라.)*




`provides improved performance` $\rightarrow$ **`improves`**
`fails to provide gains` $\rightarrow$ **`does not yield`**
`introduced by the large conductivity discontinuity` $\rightarrow$ **`under strong discontinuities`**
*(팁: 논문을 쓸 때 불필요하게 길고 장황한 표현(예: provide improved performance)을 피하라. `improves`, `yields`, `demonstrates` 같은 간결하고 강력한 학술 동사 하나로 압축하여 문장의 타격감을 높여라.)*

`\small\textit{GP outperforms DON at... PI-DON underperforms...}`
$\rightarrow$ **`%\small\textit{GP outperforms DON at... PI-DON underperforms...}`**
*(팁: 표 안에는 데이터와 아주 짧은 캡션만 남겨라. 표의 결과를 해석하고 경쟁 모델과 비교하는 산문 형태의 문장은 반드시 표 앞의 본문 단락으로 빼서 서술할 것. 단, 소스코드에서는 `%`로 주석 처리하여 "이 표의 핵심 메시지"를 메모로 남겨두어라.)*

(표를 바로 제시함)
$\rightarrow$ **`Table~\ref{tab:cost} compares error as a function of simulation cost. GNR achieves less than 10\% error with only \$3,000... while DeepONet remains above 60\% error even at \$20,000. These results highlight that GNR attains substantially better accuracy at significantly lower cost, demonstrating strong data efficiency in expensive simulation regimes.`**
*(팁: 논문에 등장하는 **모든 표와 그림 앞에는 반드시 그것을 해설하는 단락이 있어야 한다.** 1) 표가 무엇을 보여주는지 소개하고, 2) 구체적인 수치로 내 모델의 우수성을 증명하며, 3) 마지막 문장(`These results highlight/demonstrate...`)에서 그 수치가 의미하는 학술적 결론(예: data efficiency, robust extrapolation capability)을 명확히 선언하여 리뷰어의 해석을 통제하라.)*


`\begin{figure}[t]`
`\centering`
`\includegraphics[width=0.5\textwidth]{fig3_error_floor.pdf}`
`...`
`\end{figure}`
$\rightarrow$ **`\begin{wrapfigure}{l}{0.4\textwidth}`**
**`\centering`**
**`\includegraphics[width=\linewidth]{fig3_error_floor.pdf}`**
**`\vspace{-5mm}`**
`...`
**`\vspace{-10mm}`**
**`\end{wrapfigure}`**
*(팁: 학회 논문에서 지면이 부족할 때, 그림이 페이지 전체 폭을 차지할 필요가 없다면 `wrapfigure`를 사용하여 텍스트 옆에 그림을 배치하라. 이때 `\vspace`를 적극 활용하여 그림 위아래의 불필요한 여백을 깎아내면 귀중한 본문 공간을 확보할 수 있다.)*

`Key results: 1.5-5.9x lower error... 17-30x lower on semiconductor... We do not claim GNR is competitive for large data...`
$\rightarrow$ **`We introduced the GN-Operator (GNR), an analytic prior... GNR transforms operator learning into a simpler residual regression problem. ... These results suggest that incorporating analytic structure into operator learning can substantially reduce the burden on data-driven models. Future work includes extending...`**
*(팁: 결론(Conclusion) 섹션은 본문의 실험 수치를 앵무새처럼 다시 나열하는 곳이 아니다. 자잘한 수치나 "우리는 ~환경에서는 안 좋다" 같은 방어적인 변명은 모두 지워라. 대신 1) 우리 모델이 문제를 해결한 근본적인 철학(예: 복잡한 문제를 단순한 잔차 학습으로 변환), 2) 그것이 증명한 가치(데이터 효율성, 강건성), 3) 이 연구가 해당 분야에 던지는 궁극적인 메시지(해석적 구조의 통합이 모델의 부담을 줄인다)를 우아한 산문으로 선언하라. 마무리는 변명이 아닌 Future work로 미래 지향적으로 끝낼 것.)*



`\section{Method}`
`In this section, we present...`
$\rightarrow$ `\section{Method}`
**`We present...`**
*(팁: 섹션 제목 바로 밑에 "이 섹션에서는~"으로 시작하는 것은 지면 낭비다. 독자는 이미 제목을 읽었다. 군더더기 없이 바로 본론(주어+동사)으로 진입하여 글의 속도감을 높여라.)*


`\begin{proposition}`
`수학 공식...`
`\begin{tcolorbox} Implication: 이 공식의 의미는... \end{tcolorbox}`
`\end{proposition}`
$\rightarrow$ `\begin{proposition}`
`수학 공식...`
**`\end{proposition}`**
**`\begin{tcolorbox} Implication: 이 공식의 의미는... \end{tcolorbox}`**
*(팁: 엄밀한 수학적 증명/명제 환경 안에 일상어나 직관적인 해설을 섞지 마라. 수학 환경을 깔끔하게 닫은 후, 그 바깥에 해설 박스를 배치하여 '엄밀함'과 '친절함'의 시각적/논리적 경계를 명확히 하라.)*

`We consider two configurations: (1) GNR-same, which uses..., and (2) GNR-small, which uses...`
$\rightarrow$ **`We consider two configurations:`**
**`\begin{itemize}`**
**`\item \emph{GNR-same}, which uses...`**
**`\item \emph{GNR-small}, which uses...`**
**`\end{itemize}`**
*(팁: 모델의 여러 가지 설정, 3가지 기여점(Contributions) 등 병렬적인 항목을 설명할 때는 줄글 속에 욱여넣지 마라. 리뷰어가 스키밍할 때 한눈에 들어오도록 반드시 `itemize` 환경을 사용하여 시각적으로 구조화하라.)*


`is provided in Appendix` $\rightarrow$ **`is in Appendix`**
`likely due to instability under strong discontinuities` $\rightarrow$ **`due to instability under strong discontinuities`** (수학적으로 명백한 사실일 경우)
`These results demonstrate the advantage of explicitly incorporating...` $\rightarrow$ **`The results show the advantage of incorporating...`**
*(팁: 불필요한 수동태(`provided`)나 중복되는 부사(`explicitly`)는 과감히 쳐내어 문장을 가볍고 단단하게 만들어라. 특히, 내가 주장하는 원인이 단순한 추측이 아니라 해당 분야의 명백한 물리적/수학적 팩트라면, `likely` 같은 방어적 단어를 빼고 자신 있게 단정 지어라. 겸손해야 할 때와 확신해야 할 때를 구분하는 것이 고수의 글쓰기다.)*


`indicating that the network effectively captures...` $\rightarrow$ **`indicating that the network captures...`**
`(see Fig. 1a)` $\rightarrow$ **`(Fig. 1a)`**
*(팁: 수치나 결과가 이미 증명하고 있는 사실에 `effectively(효과적으로)`, `successfully(성공적으로)` 같은 주관적 부사를 덧붙여 과장하지 마라. 또한 괄호 안에서 그림이나 표를 참조할 때 굳이 `see`를 쓰지 않아도 무방하다. 군더더기를 쳐내어 문장을 단단하게 만들어라.)*

`Note that although this task is harder, our model achieves...`
$\rightarrow$ **`Although this task is harder, our model achieves...`**
*(팁: 논문을 쓸 때 `Note that(~에 주목하라)`이라는 표현을 습관적으로 쓰지 마라. 이는 구어체에 가깝고 문장을 불필요하게 늘어지게 만든다. 중요한 내용이라면 굳이 주목하라고 말하지 않아도 문맥을 통해 전달되어야 한다. 과감히 지우고 바로 본론으로 들어가라.)*