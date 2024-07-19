export default function iterateThroughObject(reportWithIterator) {
  const employeeArray = Array.from(reportWithIterator);
  return employeeArray.join(' | ');
}
