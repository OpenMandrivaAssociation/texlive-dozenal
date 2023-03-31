Name:		texlive-dozenal
Version:	47680
Release:	2
Summary:	Typeset documents using base twelve numbering (also called "dozenal")
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dozenal
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also includes a few other macros and redefines all the standard
counters to produce dozenal output. Fonts, in Roman, italic,
slanted, and boldface versions, provide ten and eleven (the
Pitman characters preferred by the Dozenal Society of Great
Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as Metafont
source and in Adobe Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/dozenal
%{_texmfdistdir}/fonts/map/dvips/dozenal
%{_texmfdistdir}/fonts/source/public/dozenal
%{_texmfdistdir}/fonts/tfm/public/dozenal
%{_texmfdistdir}/fonts/type1/public/dozenal
%{_texmfdistdir}/tex/latex/dozenal
%doc %{_texmfdistdir}/doc/fonts/dozenal
#- source
%doc %{_texmfdistdir}/source/fonts/dozenal

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
