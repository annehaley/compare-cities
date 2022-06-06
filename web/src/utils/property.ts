export default function getProperty<T, K extends keyof T>(o: T, propertyName: K) {
    const value: any = o[propertyName];
    if (parseFloat(value)) return parseFloat(value)> 0 ? value : 'N/A'
    return value
  }
