# Security Policy

## Reporting a Vulnerability

The django-remix-icon team takes security vulnerabilities seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report a Security Vulnerability

Please DO NOT report security vulnerabilities through public GitHub issues.

Instead, please follow these steps:

1. **Email**: Send your findings to [brktrl@protonmail.ch]

2. **Include details**: In your report, please include:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if available)

3. **Response timeline**:
   - We aim to acknowledge receipt of your vulnerability report within 48 hours
   - We will send you regular updates about our progress
   - After the initial reply to your report, our security team will strive to keep you informed of the progress towards a fix and announcement

### What to Expect

Once we receive your report, we will:

1. Confirm receipt of your vulnerability report
2. Assess the impact and severity of the vulnerability
3. Work on a fix and release timeline
4. Notify you when the vulnerability has been fixed
5. Publicly acknowledge your responsible disclosure (unless you prefer to remain anonymous)

## Security Best Practices When Using django-remix-icon

We recommend the following security best practices when using this package:

1. **Keep the package up-to-date**: Always use the latest version of django-remix-icon to ensure you have all security patches.

2. **Implement proper authentication**: Use strong authentication mechanisms for users who have access to the icon management interface.

3. **Use HTTPS**: Always serve your Django application over HTTPS.

4. **Regular security audits**: Periodically review the security of your Django applications.

5. **Content Security Policy**: Implement appropriate CSP headers to prevent XSS attacks.

6. **Input validation**: Always validate and sanitize user input before processing.

## Security Updates and Announcements

Security updates and announcements will be published through:

- GitHub Security Advisories
- Release notes on the project repository
- Package version updates on PyPI

## Security-Related Configuration

The django-remix-icon package is designed with security in mind. However, you should review the configuration options to ensure they meet your security requirements:

1. **Icon Upload Security**: Configure appropriate file type restrictions and size limits.
2. **Access Control**: Implement proper permission checks for icon management.
3. **Caching**: Configure appropriate caching headers for static assets.

## Vulnerability Disclosure Policy

- Public disclosure of vulnerabilities will occur after a patch has been released and users have had reasonable time to apply updates.
- We will credit security researchers who report valid vulnerabilities if they wish to be acknowledged.

Thank you for helping keep django-remix-icon and its users safe!
