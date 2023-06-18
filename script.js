// Function to extract function names from Solidity code
function extractFunctionNames(code) {
    // Regular expression pattern to match Solidity function declarations
    const pattern = /function\s+(?<name>\w+)\s*\((?<params>.*?)\)/gs;
  
    const matches = code.matchAll(pattern);
    const functions = [];
  
    for (const match of matches) {
      const name = match.groups.name;
      const params = match.groups.params.split(',');
      const cleanedParams = params.map(param => param.trim()).filter(param => param !== '');
  
      functions.push({ name, params: cleanedParams });
    }
  
    return functions;
  }
  
  // Function to extract struct information from Solidity code
  function extractStructs(code) {
    // Regular expression pattern to match Solidity struct declarations
    const pattern = /struct\s+(?<name>\w+)\s*{(?<members>[\s\S]*?)}/gs;
  
    const matches = code.matchAll(pattern);
    const structs = [];
  
    for (const match of matches) {
      const name = match.groups.name;
      const members = match.groups.members.split(';');
      const cleanedMembers = members.map(member => member.trim()).filter(member => member !== '');
  
      structs.push({ name, members: cleanedMembers });
    }
  
    return structs;
  }
  
  // Function to extract enum information from Solidity code
  function extractEnums(code) {
    // Regular expression pattern to match Solidity enum declarations
    const pattern = /enum\s+(?<name>\w+)\s*{(?<values>[\s\S]*?)}/gs;
  
    const matches = code.matchAll(pattern);
    const enums = [];
  
    for (const match of matches) {
      const name = match.groups.name;
      const values = match.groups.values.split(',');
      const cleanedValues = values.map(value => value.trim()).filter(value => value !== '');
  
      enums.push({ name, values: cleanedValues });
    }
  
    return enums;
  }
  
  // Function to extract event information from Solidity code
  function extractEvents(code) {
    // Regular expression pattern to match Solidity event declarations
    const pattern = /event\s+(?<name>\w+)\s*\((?<params>.*?)\)/gs;
  
    const matches = code.matchAll(pattern);
    const events = [];
  
    for (const match of matches) {
      const name = match.groups.name;
      const params = match.groups.params.split(',');
      const cleanedParams = params.map(param => param.trim()).filter(param => param !== '');
  
      events.push({ name, params: cleanedParams });
    }
  
    return events;
  }
  
  // Function to generate the interface from extracted data
  function generateInterface() {
    // Get the input Solidity code from the textarea
    const solidityCode = document.getElementById('solidityInput').value;
  
    // Extract data from the Solidity code
    const functions = extractFunctionNames(solidityCode);
    const structs = extractStructs(solidityCode);
    const enums = extractEnums(solidityCode);
    const events = extractEvents(solidityCode);
  
    // Generate the interface
    let interfaceHTML = '<h2>Interface</h2>';
    interfaceHTML += '<pre>interface MyContract {\n';
  
    // Generate function interfaces
    for (const func of functions) {
      const { name, params } = func;
      const functionSignature = `  function ${name}(${params.join(', ')}) external;\n`;
      interfaceHTML += functionSignature;
    }
  
    // Generate struct interfaces
    for (const struct of structs) {
      const { name, members } = struct;
      interfaceHTML += `  struct ${name} {\n`;
      for (const member of members) {
        interfaceHTML += `    ${member};\n`;
      }
      interfaceHTML += '  }\n';
    }
  
    // Generate enum interfaces
    for (const enumData of enums) {
      const { name, values } = enumData;
      interfaceHTML += `  enum ${name} {\n`;
      for (const value of values) {
        interfaceHTML += `    ${value},\n`;
      }
      interfaceHTML += '  }\n';
    }
  
    // Generate event interfaces
    for (const event of events) {
      const { name, params } = event;
      interfaceHTML += `  event ${name}(${params.join(', ')})\n`;
    }
  
    interfaceHTML += '}</pre>';
  
    // Update the interfaceOutput div with the generated HTML
    document.getElementById('interfaceOutput').innerHTML = interfaceHTML;
  }
  