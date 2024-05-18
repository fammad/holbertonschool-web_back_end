export default class Currency {
  constructor(code, name) {
  if (typeof code !== 'string') throw TypeError("Code must be string");
  this._code = code;
  if (typeof name !== 'string') throw TypeError("Name must be a string");
  this._name = name;
  }

  get code() {
    return this._code
  }
  set code(newCode) {
    if (typeof newCode !== 'string') throw TypeError("Code must be string");
    this._code = newCode;
  }
  get name() {
    return this._name
  }
  set name(newName) {
    if (typeof newName !== 'string') throw TypeError("Code must be string");
    this._code = newName;
  }
  displayFullCurrency() {
    return '${this._name} (${this._code})'
  }
}
