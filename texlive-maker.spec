%global tl_name maker
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Include Arduino or Processing code in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/maker
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/maker.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/maker.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The first version of the package allows to include Arduino or Processing
code using three different forms: writing the code directly in the LaTeX
document writing Arduino or Processing commands in line with the text
calling to Arduino or Processing files All these options support the
syntax highlighting of the official IDE.

