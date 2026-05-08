%%
%% Northeastern University doctoral dissertation template, 2026 edition.
%%
\NeedsTeXFormat{LaTeX2e}[2022/11/01]
\ProvidesClass{neudissertation}[2026/05/07 v2.0 NEU doctoral dissertation template]

\RequirePackage{kvoptions}
\SetupKeyvalOptions{family=neuclass,prefix=neuclass@}
\DeclareBoolOption[false]{blindreview}
\ProcessKeyvalOptions*

\LoadClass[a4paper,zihao=-4,fontset=none,openright,twoside]{ctexbook}

\RequirePackage{xkeyval}
\RequirePackage{etoolbox}
\RequirePackage{fontspec}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{longtable}
\RequirePackage{tabularx}
\RequirePackage{multirow}
\RequirePackage{makecell}
\RequirePackage{enumitem}
\RequirePackage{xcolor}
\RequirePackage{tikz}
\RequirePackage{eso-pic}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{bm}
\RequirePackage{indentfirst}
\RequirePackage{caption}
\RequirePackage[sort&compress]{gbt7714}
\RequirePackage[hidelinks]{hyperref}
\usetikzlibrary{calc}
\pdfstringdefDisableCommands{%
  \def\quad{ }%
}

% Base page layout matched to the Word template.
\geometry{
  a4paper,
  left=2.54cm,
  right=2.54cm,
  top=2.54cm,
  bottom=2.54cm,
  headheight=14bp,
  headsep=0.617cm,
  footskip=0.79cm
}

% Font families.
\setmainfont{Times New Roman}
\setsansfont{Arial}
\setmonofont{Courier New}
\setCJKmainfont[BoldFont=SimHei,ItalicFont=KaiTi]{SimSun}
\setCJKsansfont[
  BoldFont=SimHei,
  ItalicFont=SimHei,
  BoldItalicFont=SimHei
]{SimHei}
\setCJKmonofont{FangSong}
\setCJKfamilyfont{song}{SimSun}
\setCJKfamilyfont{hei}[
  BoldFont=SimHei,
  ItalicFont=SimHei,
  BoldItalicFont=SimHei
]{SimHei}
\setCJKfamilyfont{kai}{KaiTi}
\setCJKfamilyfont{fs}{FangSong}
\xeCJKsetup{
  % CJKecglue = {},
  PunctStyle = CCT
}

\newcommand{\song}{\CJKfamily{song}}
\newcommand{\hei}{\CJKfamily{hei}}
\newcommand{\kai}{\CJKfamily{kai}}
\newcommand{\fs}{\CJKfamily{fs}}
\newcommand{\cusong}{\bfseries}

% Chinese font sizes.
\newcommand{\chuhao}{\zihao{0}}
\newcommand{\xiaochu}{\zihao{-0}}
\newcommand{\yihao}{\zihao{1}}
\newcommand{\xiaoyi}{\zihao{-1}}
\newcommand{\erhao}{\zihao{2}}
\newcommand{\xiaoer}{\zihao{-2}}
\newcommand{\sanhao}{\zihao{3}}
\newcommand{\xiaosan}{\zihao{-3}}
\newcommand{\sihao}{\zihao{4}}
\newcommand{\xiaosi}{\zihao{-4}}
\newcommand{\wuhao}{\zihao{5}}
\newcommand{\xiaowu}{\zihao{-5}}

% Base body style matched to the Word template:
% SimSun + Times New Roman, 12 bp text with fixed 22 bp leading.
\newcommand{\thesisbodyfont}{%
  \renewcommand{\baselinestretch}{1}%
  \song
  \rmfamily
  \fontsize{12bp}{22bp}\selectfont
}
\newcommand{\thesisparagraphsetup}{%
  \setlength{\parindent}{2em}%
  \setlength{\parskip}{0bp}%
}
\newcommand{\thesisfloatsetup}{%
  \setlength{\floatsep}{6bp plus 2bp minus 2bp}%
  \setlength{\textfloatsep}{6bp plus 2bp minus 2bp}%
  \setlength{\intextsep}{6bp plus 2bp minus 2bp}%
  \setlength{\abovedisplayskip}{8bp plus 2bp minus 2bp}%
  \setlength{\belowdisplayskip}{8bp plus 2bp minus 2bp}%
  \setlength{\abovedisplayshortskip}{4bp plus 2bp minus 1bp}%
  \setlength{\belowdisplayshortskip}{8bp plus 2bp minus 2bp}%
}
\AtBeginDocument{%
  \thesisbodyfont
  \thesisparagraphsetup
  \thesisfloatsetup
  \raggedbottom
}

\makeatletter

% Metadata defaults.
\newcommand{\neu@classification}{}
\newcommand{\neu@securitylevel}{}
\newcommand{\neu@udc}{}
\newcommand{\neu@studentid}{}
\newcommand{\neu@titlecn}{东北大学博士学位论文题名}
\newcommand{\neu@titleen}{Doctoral Dissertation Title of Northeastern University}
\newcommand{\neu@authorcnraw}{作者姓名}
\newcommand{\neu@authorenraw}{Author Name}
\newcommand{\neu@collegecn}{学院名称}
\newcommand{\neu@majorcn}{学科专业名称}
\newcommand{\neu@majoren}{Discipline}
\newcommand{\neu@degreelevel}{博士}
\newcommand{\neu@discipline}{工学}
\newcommand{\neu@supervisorcnraw}{导师姓名}
\newcommand{\neu@supervisortitlecn}{教授}
\newcommand{\neu@supervisoraffiliationcn}{东北大学}
\newcommand{\neu@supervisorenraw}{Professor Supervisor}
\newcommand{\neu@cosupervisorcnraw}{}
\newcommand{\neu@cosupervisortitlecn}{}
\newcommand{\neu@cosupervisoraffiliationcn}{}
\newcommand{\neu@cosupervisorenraw}{}
\newcommand{\neu@submitdate}{20xx年6月}
\newcommand{\neu@defensedate}{20xx年6月}
\newcommand{\neu@degreedate}{20xx年7月}
\newcommand{\neu@defensechair}{答辩委员会主席}
\newcommand{\neu@coverdatecn}{20xx年7月}
\newcommand{\neu@coverdateen}{July 20xx}
\newcommand{\neu@onlinerelease}{两年}
\newcommand{\neu@signaturedate}{}
\newcommand{\neu@authorsignature}{}
\newcommand{\neu@supervisorsignature}{}
\newcommand{\neu@signatureheight}{8mm}
\newif\ifneu@header@twentysix
\neu@header@twentysixtrue

\define@key{neudissertation}{classification}{\renewcommand{\neu@classification}{#1}}
\define@key{neudissertation}{security-level}{\renewcommand{\neu@securitylevel}{#1}}
\define@key{neudissertation}{udc}{\renewcommand{\neu@udc}{#1}}
\define@key{neudissertation}{student-id}{\renewcommand{\neu@studentid}{#1}}
\define@key{neudissertation}{title-cn}{\renewcommand{\neu@titlecn}{#1}}
\define@key{neudissertation}{title-en}{\renewcommand{\neu@titleen}{#1}}
\define@key{neudissertation}{author-cn}{\renewcommand{\neu@authorcnraw}{#1}}
\define@key{neudissertation}{author-en}{\renewcommand{\neu@authorenraw}{#1}}
\define@key{neudissertation}{college-cn}{\renewcommand{\neu@collegecn}{#1}}
\define@key{neudissertation}{major-cn}{\renewcommand{\neu@majorcn}{#1}}
\define@key{neudissertation}{major-en}{\renewcommand{\neu@majoren}{#1}}
\define@key{neudissertation}{degree-level}{\renewcommand{\neu@degreelevel}{#1}}
\define@key{neudissertation}{discipline}{\renewcommand{\neu@discipline}{#1}}
\define@key{neudissertation}{supervisor-cn}{\renewcommand{\neu@supervisorcnraw}{#1}}
\define@key{neudissertation}{supervisor-title-cn}{\renewcommand{\neu@supervisortitlecn}{#1}}
\define@key{neudissertation}{supervisor-affiliation-cn}{\renewcommand{\neu@supervisoraffiliationcn}{#1}}
\define@key{neudissertation}{supervisor-en}{\renewcommand{\neu@supervisorenraw}{#1}}
\define@key{neudissertation}{cosupervisor-cn}{\renewcommand{\neu@cosupervisorcnraw}{#1}}
\define@key{neudissertation}{cosupervisor-title-cn}{\renewcommand{\neu@cosupervisortitlecn}{#1}}
\define@key{neudissertation}{cosupervisor-affiliation-cn}{\renewcommand{\neu@cosupervisoraffiliationcn}{#1}}
\define@key{neudissertation}{cosupervisor-en}{\renewcommand{\neu@cosupervisorenraw}{#1}}
\define@key{neudissertation}{submit-date}{\renewcommand{\neu@submitdate}{#1}}
\define@key{neudissertation}{defense-date}{\renewcommand{\neu@defensedate}{#1}}
\define@key{neudissertation}{degree-date}{\renewcommand{\neu@degreedate}{#1}}
\define@key{neudissertation}{defense-chair}{\renewcommand{\neu@defensechair}{#1}}
\define@key{neudissertation}{cover-date-cn}{\renewcommand{\neu@coverdatecn}{#1}}
\define@key{neudissertation}{cover-date-en}{\renewcommand{\neu@coverdateen}{#1}}
\define@key{neudissertation}{online-release}{\renewcommand{\neu@onlinerelease}{#1}}
\define@key{neudissertation}{signature-date}{\renewcommand{\neu@signaturedate}{#1}}
\define@key{neudissertation}{author-signature}{\renewcommand{\neu@authorsignature}{#1}}
\define@key{neudissertation}{supervisor-signature}{\renewcommand{\neu@supervisorsignature}{#1}}
\define@key{neudissertation}{signature-height}{\renewcommand{\neu@signatureheight}{#1}}
\define@key{neudissertation}{header-2026}[true]{%
  \edef\neu@headerflag{#1}%
  \ifdefstring{\neu@headerflag}{true}{%
    \neu@header@twentysixtrue
  }{%
    \ifdefstring{\neu@headerflag}{false}{%
      \neu@header@twentysixfalse
    }{%
      \ClassError{neudissertation}{Invalid value for `header-2026': #1}{Use `true' or `false'.}%
    }%
  }%
}
% 注意：`header-2026` 为首选配置键（保留）。
% 旧的 `header-style` 与 `header-2026` 功能等价且会导致重复键名，
% 因此在本模板中移除 `header-style` 的声明。请使用：
%   \neudisetup{header-2026=true}
% 或
%   \neudisetup{header-2026=false}
% 来控制页眉样式（true 为 2026 新样式，false 为 legacy）。
\newcommand{\neudisetup}[1]{\setkeys{neudissertation}{#1}}

\newcommand{\neu@authorcn}{\ifneuclass@blindreview 第一作者\else \neu@authorcnraw\fi}
\newcommand{\neu@authoren}{\ifneuclass@blindreview Author\else \neu@authorenraw\fi}
\newcommand{\neu@supervisorcn}{\ifneuclass@blindreview 导师\else \neu@supervisorcnraw\fi}
\newcommand{\neu@supervisoren}{\ifneuclass@blindreview Supervisor\else \neu@supervisorenraw\fi}
\newcommand{\neu@cosupervisorcn}{\ifneuclass@blindreview 协助指导教师\else \neu@cosupervisorcnraw\fi}
\newcommand{\neu@cosupervisoren}{\ifneuclass@blindreview Co-supervisor\else \neu@cosupervisorenraw\fi}

\newcommand{\neu@entry}[2]{\underline{\makebox[#1][c]{#2}}}
\newcommand{\neu@spreadbox}[2]{{\hbadness=10000\makebox[#1][s]{#2}}}
\newcommand{\neu@coverlabel}[1]{\neu@spreadbox{42mm}{#1}}
\newcommand{\neu@coverlabelbox}[1]{\neu@spreadbox{37mm}{#1}}
\newcommand{\neu@coverleftline}[3]{%
  \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (32.2,#1)
    {\song\sihao \neu@coverlabelbox{#2}\hspace{2.1mm}#3};
}
\newcommand{\neu@coverpairline}[5]{%
  \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (32.2,#1)
    {\song\sihao \neu@coverlabelbox{#2}\hspace{2.1mm}#3};
  \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (96.8,#1)
    {\song\sihao \neu@coverlabelbox{#4}\hspace{2.1mm}#5};
}
\newcommand{\neu@blankpage}{%
  \clearpage
  \thispagestyle{empty}
  \null
  \clearpage
}

% Headers and footers.
\newcommand{\neu@legacyheadtitle}{东北大学\neu@degreelevel 学位论文}
\newcommand{\neu@setheaderfields}{%
  \fancyheadoffset[LE,LO,RE,RO]{0pt}%
  \ifneu@header@twentysix
    \fancyhead[C]{\wuhao\kai\nouppercase{\leftmark}}%
  \else
    \fancyhead[L]{\wuhao\kai \neu@legacyheadtitle}%
    \fancyhead[R]{\wuhao\kai\nouppercase{\leftmark}}%
  \fi
}
\newcommand{\neu@headrule}{%
  \hrule width\textwidth height\headrulewidth \vskip 1pt
}
\pagestyle{fancy}
\fancyhf{}
\neu@setheaderfields
\fancyfoot[C]{\xiaowu -\thepage-}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\headrule}{\neu@headrule}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}
  \neu@setheaderfields
  \fancyfoot[C]{\xiaowu -\thepage-}
  \renewcommand{\headrulewidth}{0.4pt}
  \renewcommand{\headrule}{\neu@headrule}
  \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{neunumberonly}{%
  \fancyhf{}
  \fancyfoot[C]{\xiaowu -\thepage-}
  \renewcommand{\headrule}{}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{neuempty}{%
  \fancyhf{}
  \renewcommand{\headrule}{}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

\renewcommand{\chaptermark}[1]{%
  \ifnum\value{chapter}>0
    \ifneu@header@twentysix
      \markboth{第~\thechapter~章\quad #1}{}
    \else
      \markboth{第\thechapter 章\quad #1}{}
    \fi
  \else
    \markboth{#1}{}
  \fi
}

% Chapter and section titles.
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
\ctexset{
  chapter = {
    name = {第~,~章},
    number = \arabic{chapter},
    aftername = \quad
  },
  section = {
    format = \sanhao\hei\raggedright,
    number = \thesection
  },
  subsection = {
    format = \sihao\hei\raggedright,
    number = \thesubsection
  },
  subsubsection = {
    format = \xiaosi\hei\raggedright,
    number = \thesubsubsection
  }
}
\titleformat{\chapter}[block]
  {\centering\erhao\hei}
  {第~\thechapter~章}
  {1em}
  {}
\titleformat{name=\chapter,numberless}[block]
  {\centering\erhao\hei}
  {}
  {0pt}
  {}
\titlespacing*{\chapter}{0pt}{0pt}{23pt}
\titleformat{\section}{\sanhao\hei}{\thesection}{0.75em}{}
\titlespacing*{\section}{0pt}{20pt}{13pt}
\titleformat{\subsection}{\sihao\hei}{\thesubsection}{0.75em}{}
\titlespacing*{\subsection}{0pt}{16pt}{14.5pt}
\titleformat{\subsubsection}{\xiaosi\hei}{\thesubsubsection}{0.75em}{}
\titlespacing*{\subsubsection}{0pt}{10pt}{6pt}
\titleformat{\paragraph}[hang]{\xiaosi\hei}{\theparagraph}{0.75em}{}
\titlespacing*{\paragraph}{0pt}{6pt}{0.75em}

\renewcommand{\contentsname}{目\quad 录}
\renewcommand{\bibname}{参考文献}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
\renewcommand{\appendixname}{附录}

\titlecontents{chapter}
  [0em]{\hei}
  {\thecontentslabel\quad}
  {}
  {\titlerule*[0.5pc]{.}\contentspage}
\titlecontents{section}
  [2em]{}
  {\thecontentslabel\quad}
  {}
  {\titlerule*[0.5pc]{.}\contentspage}
\titlecontents{subsection}
  [4em]{}
  {\thecontentslabel\quad}
  {}
  {\titlerule*[0.5pc]{.}\contentspage}
\titlecontents{subsubsection}
  [6em]{}
  {\thecontentslabel\quad}
  {}
  {\titlerule*[0.5pc]{.}\contentspage}

% Matter transitions.
\renewcommand{\frontmatter}{%
  \cleardoublepage
  \pagenumbering{Roman}
  \setcounter{page}{1}
  \@mainmatterfalse
  \pagestyle{fancy}
}
\renewcommand{\mainmatter}{%
  \cleardoublepage
  \pagenumbering{arabic}
  \setcounter{page}{1}
  \@mainmattertrue
  \pagestyle{fancy}
}
\renewcommand{\backmatter}{%
  \cleardoublepage
  \@mainmatterfalse
  \pagestyle{fancy}
}
\renewcommand{\cleardoublepage}{%
  \clearpage
  \if@twoside
    \ifodd\c@page\else
      \thispagestyle{neuempty}
      \hbox{}\newpage
    \fi
  \fi
}

% Covers.
\newcommand{\makeneucovers}{%
  \begingroup
  \pagestyle{neuempty}
  \thispagestyle{neuempty}
  \AddToShipoutPictureFG*{%
    \AtPageUpperLeft{%
      \begin{tikzpicture}[x=1mm,y=-1mm]
    \begin{scope}
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.1,28.4)
        {\song\sihao 分类号};
      \draw[line width=0.4pt,line cap=butt] (44.9,33.5) -- (89.4,33.5);
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (96.9,28.4)
        {\song\sihao 密级};
      \draw[line width=0.4pt,line cap=butt] (109.0,33.5) -- (133.8,33.5);
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.1,40.4)
        {\song\sihao UDC};
      \draw[line width=0.4pt,line cap=butt] (42.8,44.5) -- (89.8,44.5);

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,54.9)
        {\song\erhao \neu@spreadbox{54.3mm}{学位论文}};
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.2,72.0)
        {\hei\xiaoer \neu@titlecn};

      \neu@coverleftline{100.2}{作者姓名：}{\neu@authorcn}
      \neu@coverleftline{111.3}{作者学号：}{\neu@studentid}
      \ifdefempty{\neu@cosupervisorcnraw}{%
        \neu@coverleftline{122.2}{指导教师：}{\neu@supervisorcn\quad \neu@supervisortitlecn}
        \node[anchor=north,inner sep=0pt,outer sep=0pt] at (103.3,133.2)
          {\song\sihao \neu@supervisoraffiliationcn};
      }{%
        \neu@coverleftline{122.2}{指导教师：}{\neu@supervisorcn\quad \neu@supervisortitlecn\qquad \neu@supervisoraffiliationcn}
        \neu@coverleftline{133.2}{}{\neu@cosupervisorcn\quad \neu@cosupervisortitlecn\qquad \neu@cosupervisoraffiliationcn}
      }
      \neu@coverpairline{144.2}{申请学位级别：}{\neu@degreelevel}{学科类别：}{\neu@discipline}
      \neu@coverleftline{155.2}{学科专业名称：}{\neu@majorcn}
      \neu@coverpairline{166.2}{论文提交日期：}{\neu@submitdate}{论文答辩日期：}{\neu@defensedate}
      \neu@coverpairline{177.2}{学位授予日期：}{\neu@degreedate}{答辩委员会主席：}{\neu@defensechair}

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.1,221.3)
        {\song\sihao \neu@spreadbox{34.7mm}{东北大学}};
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.1,232.4)
        {\song\sihao \neu@coverdatecn};
    \end{scope}
      \end{tikzpicture}%
    }%
  }%
  \null
  \cleardoublepage
  \thispagestyle{neuempty}
  \AddToShipoutPictureFG*{%
    \AtPageUpperLeft{%
      \begin{tikzpicture}[x=1mm,y=-1mm]
    \begin{scope}
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (82.0,29.4)
        {\sihao\bfseries A Dissertation in \neu@majoren};

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,55.9)
        {\begin{minipage}{160mm}
          \centering\erhao\bfseries\linespread{1.2}\selectfont \neu@titleen
        \end{minipage}};

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,95.3)
        {\sihao by \neu@authoren};
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,122.8)
        {\sihao Supervisor: \neu@supervisoren};
      \ifdefempty{\neu@cosupervisorenraw}{}{%
        \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,133.4)
          {\sihao Co-supervisor: \neu@cosupervisoren};
      }

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,232.7)
        {\sanhao\bfseries Northeastern University};
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,243.8)
        {\sanhao\bfseries \neu@coverdateen};
    \end{scope}
      \end{tikzpicture}%
    }%
  }%
  \null
  \cleardoublepage
  \endgroup
}
\let\maketitle\makeneucovers

% Declaration and authorization.
\newcommand{\neu@releasebox}[1]{%
  #1\ \ifdefstring{\neu@onlinerelease}{#1}{$\mbox{\ooalign{$\checkmark$\cr\hidewidth$\square$\hidewidth\cr}}$}{$\square$}
}
\newcommand{\neu@declarationsigndate}{%
  \ifdefempty{\neu@signaturedate}{\neu@coverdatecn}{\neu@signaturedate}%
}
\newcommand{\neu@signaturegraphic}[2]{%
  \ifdefempty{#1}{}{%
    \IfFileExists{#1}{%
      \raisebox{-0.35\height}{\includegraphics[height=#2,keepaspectratio]{#1}}%
    }{%
      \ClassWarning{neudissertation}{Signature file `#1' not found}%
    }%
  }%
}
\newcommand{\neu@authorsignaturegraphic}{\neu@signaturegraphic{\neu@authorsignature}{\neu@signatureheight}}
\newcommand{\neu@supervisorsignaturegraphic}{\neu@signaturegraphic{\neu@supervisorsignature}{\neu@signatureheight}}
\newcommand{\makeneudeclaration}{%
  \cleardoublepage
  \markboth{}{}
  \addcontentsline{toc}{chapter}{独创性声明}
  \thispagestyle{neunumberonly}
  \AddToShipoutPictureFG*{%
    \AtPageUpperLeft{%
      \begin{tikzpicture}[x=1mm,y=-1mm]
    \begin{scope}
      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,27.3)
        {\hei\erhao 独创性声明};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (40.0,45.1)
        {\song\sihao\makebox[139.7mm][s]{本人声明，所呈交的学位论文是在导师的指导下完成的。论文中取}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,56.1)
        {\song\sihao\makebox[149.5mm][s]{得的研究成果除加以标注和致谢的地方外，不包含其他人已经发表或}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,67.1)
        {\song\sihao\makebox[149.3mm][s]{撰写过的研究成果，也不包括本人为获得其他学位而使用过的材料。与}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,78.1)
        {\song\sihao\makebox[149.4mm][s]{我一同工作的同志对本研究所做的任何贡献均已在论文中作了明确的}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,89.2)
        {\song\sihao 说明并表示谢意。};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (107.6,102.9)
        {\song\sihao 学位论文作者签名：\neu@authorsignaturegraphic};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (106.6,117.5)
        {\song\sihao 日\quad\quad 期：\neu@declarationsigndate};

      \node[anchor=north,inner sep=0pt,outer sep=0pt] at (105.0,133.5)
        {\hei\erhao 学位论文版权使用授权书};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (40.0,151.3)
        {\song\sihao\makebox[139.7mm][s]{本学位论文作者和指导教师完全了解学校有关保留、使用学位论}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,162.3)
        {\song\sihao\makebox[149.2mm][s]{文的规定：即学校有权保留并向国家有关部门或机构送交论文的复印}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,173.3)
        {\song\sihao\makebox[149.6mm][s]{件和磁盘，允许论文被查阅和借阅。本人同意学校可以将学位论文的全}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.2,184.3)
        {\song\sihao 部或部分内容编入有关数据库进行检索、交流。};

      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (39.9,206.3)
        {\song\sihao 作者和导师同意网上交流的时间为作者获得学位后：};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (39.9,222.8)
        {\song\sihao \neu@releasebox{半年}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (72.0,222.8)
        {\song\sihao \neu@releasebox{一年}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (104.0,222.8)
        {\song\sihao \neu@releasebox{一年半}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (136.0,222.8)
        {\song\sihao \neu@releasebox{两年}};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.0,239.4)
        {\song\sihao 学位论文作者签名：\neu@authorsignaturegraphic};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (108.0,239.4)
        {\song\sihao 导师签名：\neu@supervisorsignaturegraphic};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (30.0,250.4)
        {\song\sihao 签字日期：\neu@declarationsigndate};
      \node[anchor=north west,inner sep=0pt,outer sep=0pt] at (108.0,250.4)
        {\song\sihao 签字日期：\neu@declarationsigndate};
    \end{scope}
      \end{tikzpicture}%
    }%
  }%
  \null
}

% Abstract environments.
\newcommand{\neuabstracttitle}[1]{%
  \par\vspace*{6bp}%
  {\centering \hei\bfseries\fontsize{22bp}{24bp}\selectfont #1\par}%
  \vspace{18bp}%
}

\newcommand{\cnkeywords}[1]{%
  \par\vspace{1em}%
  \noindent{\hei 关键词：}\song #1\par
}

\newcommand{\enkeywords}[1]{%
  \par\vspace{1em}%
  \noindent{\bfseries Key words:} #1\par
}

% ---------- 中文摘要环境 ----------
% 命名规范：中文相关环境/宏统一使用 "-cn" 后缀，这里使用 `abstract-cn`。
\newenvironment{abstract-cn}{%
  \cleardoublepage
  \markboth{摘\quad 要}{}
  \addcontentsline{toc}{chapter}{摘\quad 要}
  \thispagestyle{plain}
  \neuabstracttitle{摘\hspace{1em}要}
  \thesisbodyfont
  \thesisparagraphsetup
}{%
  \par
}
\newenvironment{enabstract}{%
  \cleardoublepage
  \markboth{Abstract}{}
  \addcontentsline{toc}{chapter}{Abstract}
  \thispagestyle{plain}
  \neuabstracttitle{Abstract}
}{}

% Caption, reference, list, and bibliography helpers.
\numberwithin{equation}{chapter}
\numberwithin{figure}{chapter}
\numberwithin{table}{chapter}
\DeclareCaptionFont{neuwuhao}{\wuhao}
\captionsetup{font=neuwuhao,labelsep=space,skip=3bp}
\captionsetup[figure]{position=bottom,aboveskip=3bp,belowskip=0bp}
\captionsetup[table]{position=top,aboveskip=0bp,belowskip=3bp}
\newcommand{\neufigcaption}[3]{%
  \caption{#2\label{#1}}%
  {\centering\wuhao Fig.~\ref{#1}\quad #3\par}%
}
\newcommand{\neutabcaption}[3]{%
  \caption{#2\label{#1}}%
  {\centering\wuhao Table~\ref{#1}\quad #3\par}%
  \vspace{3bp}%
}
\newcommand{\neufigref}[1]{图~\ref{#1}}
\newcommand{\neutabref}[1]{表~\ref{#1}}
\newcommand{\neueqref}[1]{式（\ref{#1}）}
\@namedef{bibstyle@gbt7714-unsrt}{\bibstyle@super}
\NewDocumentCommand{\upcite}{om}{%
  \IfNoValueTF{#1}{\citep{#2}}{\citep[#1]{#2}}%
}
\NewDocumentCommand{\inlinecite}{om}{%
  \begingroup
  \citestyle{inline}%
  \IfNoValueTF{#1}{\citep{#2}}{\citep[#1]{#2}}%
  \endgroup
}
\let\twofigcaption\neufigcaption
\let\twotabcaption\neutabcaption
\let\figref\neufigref
\let\tabref\neutabref
\let\equref\neueqref

\AtBeginEnvironment{thebibliography}{%
  \thesisbodyfont
  \thesisparagraphsetup
  \setlength{\itemsep}{0bp}%
  \setlength{\parsep}{0bp}%
  \setlength{\topsep}{0bp}%
  \setlength{\partopsep}{0bp}%
}

\setlist{nosep}
\setlist[enumerate]{leftmargin=2em}
\setlist[itemize]{leftmargin=2em}
\bibliographystyle{gbt7714-unsrt}

\makeatother

\endinput
