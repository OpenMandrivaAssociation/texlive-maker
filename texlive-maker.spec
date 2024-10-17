Name:		texlive-maker
Version:	44823
Release:	2
Summary:	Include Arduino or Processing code in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/maker
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maker.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/maker.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The first version of the package allows to include Arduino or
Processing code using three different forms: writing the code
directly in the LaTeX document writing Arduino or Processing
commands in line with the text calling to Arduino or Processing
files All these options support the syntax highlighting of the
oficial IDE.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/maker
%doc %{_texmfdistdir}/doc/latex/maker

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
