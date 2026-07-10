%global tl_name dozenal
%global tl_revision 75722

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.2
Release:	%{tl_revision}.1
Summary:	Typeset documents using base twelve numbering (also called dozenal)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/dozenal
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dozenal.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes a macro
by David Kastrup for converting positive whole numbers to dozenal from
decimal (base ten) representation. The package also includes a few other
macros and redefines all the standard counters to produce dozenal
output. Fonts, in Roman, italic, slanted, and boldface versions, provide
ten and eleven (the Pitman characters preferred by the Dozenal Society
of Great Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as Metafont source and in
Adobe Type 1 format.

