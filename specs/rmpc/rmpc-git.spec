%global gh_user mierak
%global gh_repo rmpc
%global common_description A configurable, terminal based Media Player Client with album art support via various terminal image protocols
%global pkgname rmpc-master
%define debug_package %{nil}

Name:           rmpc-git
# renovate: datasource=github-releases depName=mierak/rmpc versioning=semver-coerced
Version:        %(date --date=now '+%%Y.%%m.%%d')
Release:        1%{?dist}
Summary:        %{common_description}
License:        BSD-3-Clause
URL:            https://mierak.github.io/rmpc/
Source0:        https://github.com/%{gh_user}/%{gh_repo}/archive/refs/heads/main.tar.gz
BuildRequires:  cargo
Requires:       mpd
Requires:       cava

%description
%{common_description}

%prep
%setup -q -n %{pkgname}

%build
cargo b --release

%install
install -Dm 755 %{_builddir}/%{pkgname}/target/release/rmpc -t %{buildroot}%{_bindir}
install -Dm 644 %{_builddir}/%{pkgname}/target/man/rmpc.1 -t %{buildroot}/%{_mandir}/man1/
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/rmpc.bash -t %{buildroot}/%{bash_completions_dir}
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/rmpc.fish -t %{buildroot}/%{fish_completions_dir}
install -Dm 644 %{_builddir}/%{pkgname}/target/completions/_rmpc -t %{buildroot}/%{zsh_completions_dir}

%files
%license LICENSE
%{_bindir}/rmpc
%{_mandir}/man1/rmpc.1*
%{bash_completions_dir}/rmpc.bash
%{fish_completions_dir}/rmpc.fish
%{zsh_completions_dir}/_rmpc

%changelog
%autochangelog
